# templates.py

# --- 1. MUTUAL NDA ---
NDA_TEMPLATE = """MUTUAL NON-DISCLOSURE AGREEMENT (NDA)

This Agreement is entered into as of [Date], by and between [Party A Name] and [Party B Name].

1. PURPOSE: The Parties wish to explore a business relationship and may disclose confidential information.
2. CONFIDENTIAL INFORMATION: Includes business plans, technical data, customer lists, and financial info.
3. OBLIGATIONS: Each Party agrees to use information ONLY for the specified purpose and not disclose it to third parties.
4. TERM: This agreement is valid for two (2) years from the date of disclosure.
5. JURISDICTION: This Agreement is governed by the laws of India. Courts in [City, State] shall have jurisdiction.

SIGNATURES:
Party A: ____________________    Party B: ____________________
"""

# --- 2. SERVICE AGREEMENT ---
SERVICE_TEMPLATE = """MASTER SERVICE AGREEMENT

This Agreement is made between [Service Provider Name] ("Provider") and [Client Name] ("Client").

1. SERVICES: The Provider agrees to perform the following services: [Description of Work].
2. PAYMENT: Client shall pay Provider [Amount] within [Number] days of receiving an invoice.
3. TERM & TERMINATION: Either party may terminate this agreement with [30] days' written notice.
4. INTELLECTUAL PROPERTY: Upon full payment, all work product developed shall belong to the Client.
5. CONFIDENTIALITY: Provider shall keep all Client data confidential.
6. LIMITATION OF LIABILITY: Neither party shall be liable for indirect or consequential damages.

SIGNATURES:
Provider: ____________________    Client: ____________________
"""

# --- 3. EMPLOYMENT OFFER LETTER ---
OFFER_TEMPLATE = """EMPLOYMENT OFFER LETTER

Date: [Current Date]
To: [Candidate Name]

Subject: Offer of Employment

Dear [Candidate Name],

We are pleased to offer you the position of [Job Title] at [Company Name].

1. REMUNERATION: Your annual CTC will be [Amount]/- payable monthly.
2. PROBATION: You will be on probation for a period of [3 or 6] months.
3. JOINING DATE: Your expected date of joining is [Date].
4. TERMINATION: During probation, either party can terminate with [15] days' notice. After confirmation, the notice period is [30 or 60] days.
5. DUTIES: Your duties will be as discussed during the interview process.

Welcome to the team!

For [Company Name],
(Authorized Signatory)
"""

# --- THE DICTIONARY MAP ---
TEMPLATES = {
    "Mutual NDA (Standard)": NDA_TEMPLATE,
    "Service Agreement (SME)": SERVICE_TEMPLATE,
    "Employment Offer Letter": OFFER_TEMPLATE
}