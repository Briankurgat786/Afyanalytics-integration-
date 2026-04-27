# Afyanalytics External Platform Integration

## Overview
This project demonstrates integration with the Afyanalytics Health Platform using a secure two-step authentication handshake process.

The system:
- Initiates a handshake with the API
- Receives a time-limited handshake token
- Completes authentication using the token
- Handles basic error scenarios

---

## Tech Stack
- Python 3
- Requests library
- dotenv (for secure environment variables)

---

## Authentication Flow

1. **Initiate Handshake**
   - Sends platform credentials to `/initiate-handshake`
   - Receives a handshake token (valid for 15 minutes)

2. **Complete Handshake**
   - Sends token to `/complete-handshake`
   - Receives:
     - Access Token
     - Refresh Token

---

## Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/YOUR_USERNAME/afyanalytics-integration.git
cd afyanalytics-integration