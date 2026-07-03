from fastapi import APIRouter, File, UploadFile, HTTPException
from app.database import get_connection
from app.services.s3_storage import upload_ticket_file

router = APIRouter(prefix="/tickets", tags=["attachments"])


@router.post("/{ticket_id}/attachments")
def upload_attachment(ticket_id: int, file: UploadFile = File(...)):
    with get_connection() as conn:
        ticket = conn.execute(
            "SELECT * FROM tickets WHERE id = ?",
            (ticket_id,),
        ).fetchone()

        if ticket is None:
            raise HTTPException(status_code=404, detail="Ticket not found")

    uploaded = upload_ticket_file(ticket_id, file)

    return {
        "message": "File uploaded successfully",
        "ticket_id": ticket_id,
        "s3_bucket": uploaded["bucket"],
        "s3_key": uploaded["key"],
        "filename": uploaded["filename"],
        "content_type": uploaded["content_type"],
    }
