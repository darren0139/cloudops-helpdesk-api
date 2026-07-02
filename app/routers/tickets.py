from fastapi import APIRouter, HTTPException
from app.database import get_connection
from app.schemas import TicketCreate, TicketUpdate, TicketOut, AIClassifyRequest, AIClassifyResponse
from app.services.ai_classifier import classify_ticket

router = APIRouter(prefix="/tickets", tags=["tickets"])

def row_to_ticket(row) -> TicketOut:
    return TicketOut(
        id=row["id"],
        title=row["title"],
        description=row["description"],
        category=row["category"],
        priority=row["priority"],
        status=row["status"],
        created_at=row["created_at"],
    )

@router.post("/", response_model=TicketOut, status_code=201)
def create_ticket(payload: TicketCreate):
    with get_connection() as conn:
        cursor = conn.execute(
            """
            INSERT INTO tickets (title, description, category, priority, status)
            VALUES (?, ?, ?, ?, 'open')
            """,
            (payload.title, payload.description, payload.category, payload.priority),
        )
        conn.commit()
        ticket_id = cursor.lastrowid
        row = conn.execute("SELECT * FROM tickets WHERE id = ?", (ticket_id,)).fetchone()
        return row_to_ticket(row)

@router.get("/", response_model=list[TicketOut])
def list_tickets():
    with get_connection() as conn:
        rows = conn.execute("SELECT * FROM tickets ORDER BY id DESC").fetchall()
        return [row_to_ticket(row) for row in rows]

@router.get("/{ticket_id}", response_model=TicketOut)
def get_ticket(ticket_id: int):
    with get_connection() as conn:
        row = conn.execute("SELECT * FROM tickets WHERE id = ?", (ticket_id,)).fetchone()
        if row is None:
            raise HTTPException(status_code=404, detail="Ticket not found")
        return row_to_ticket(row)

@router.patch("/{ticket_id}", response_model=TicketOut)
def update_ticket(ticket_id: int, payload: TicketUpdate):
    updates = []
    values = []

    if payload.status is not None:
        updates.append("status = ?")
        values.append(payload.status)

    if payload.priority is not None:
        updates.append("priority = ?")
        values.append(payload.priority)

    if not updates:
        raise HTTPException(status_code=400, detail="No update fields provided")

    values.append(ticket_id)

    with get_connection() as conn:
        existing = conn.execute("SELECT * FROM tickets WHERE id = ?", (ticket_id,)).fetchone()
        if existing is None:
            raise HTTPException(status_code=404, detail="Ticket not found")

        conn.execute(f"UPDATE tickets SET {', '.join(updates)} WHERE id = ?", values)
        conn.commit()

        row = conn.execute("SELECT * FROM tickets WHERE id = ?", (ticket_id,)).fetchone()
        return row_to_ticket(row)

@router.post("/classify", response_model=AIClassifyResponse)
def classify(payload: AIClassifyRequest):
    return classify_ticket(payload.title, payload.description)
