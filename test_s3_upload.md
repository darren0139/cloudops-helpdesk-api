# Test S3 Upload

1. Create a ticket first using `/docs`:

```json
{
  "title": "VPN cannot connect",
  "description": "User cannot connect from home",
  "category": "network",
  "priority": "high"
}
```

2. Go to:

```text
POST /tickets/{ticket_id}/attachments
```

3. Enter ticket ID, e.g. `1`.
4. Upload a small `.txt` file or screenshot.
5. Check your S3 bucket:

```text
tickets/1/<uuid>-filename.png
```

Common errors:

- AccessDenied: IAM role/policy/bucket name problem.
- Missing bucket env var: forgot `-e S3_BUCKET_NAME=...`.
- Endpoint missing: forgot to include attachments router in main.py.
