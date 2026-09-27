"""
Verification test for Flask portfolio application.
"""
from app import app
import json

client = app.test_client()

def test_routes():
    print("Testing GET / ...")
    r1 = client.get('/')
    assert r1.status_code == 200, f"Expected 200, got {r1.status_code}"
    assert b"Yatin Kumar Singh" in r1.data
    assert b"Accenture" in r1.data
    assert b"Snowflake" in r1.data
    print("[PASS] GET / passed")

    print("Testing GET /resume ...")
    r2 = client.get('/resume')
    assert r2.status_code == 200, f"Expected 200, got {r2.status_code}"
    assert b"Print / Save as PDF" in r2.data
    print("[PASS] GET /resume passed")

    print("Testing GET /api/profile ...")
    r3 = client.get('/api/profile')
    assert r3.status_code == 200
    data = json.loads(r3.data)
    assert data["name"] == "Yatin Kumar Singh"
    assert data["role"] == "Senior Data Engineer"
    print("[PASS] GET /api/profile passed")

    print("Testing POST /api/contact ...")
    r4 = client.post('/api/contact', json={
        "name": "Recruiter Jane",
        "email": "jane@techcorp.com",
        "subject": "Data Engineer Opportunity",
        "message": "We have an open Senior Data Engineer role."
    })
    assert r4.status_code == 200
    res = json.loads(r4.data)
    assert res["status"] == "success"
    print("[PASS] POST /api/contact passed")

    print("\nALL TESTS PASSED SUCCESSFULLY!")

if __name__ == '__main__':
    test_routes()
