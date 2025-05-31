#!/usr/bin/env python3
"""
Quick API Test Script for Quantum HR Intelligence Platform
"""

import requests
import json

def test_neural_talent_endpoint():
    """Test the neural talent analysis endpoint"""
    print("🧬 Testing Neural Talent Analysis Endpoint...")
    
    url = "http://localhost:8000/api/quantum/v1/neural-talent-analysis"
    data = {
        "candidate_data": {
            "name": "Alex Chen",
            "email": "alex.chen@email.com",
            "phone": "(555) 123-4567",
            "position_applied": "Senior Software Engineer",
            "experience_years": 6,
            "job_requirements": {
                "required_skills": ["Python", "React", "AWS", "PostgreSQL"],
                "experience_years": 5,
                "education_required": "Bachelor's degree",
                "position": "Senior Software Engineer"
            }
        },
        "resume_text": """
        ALEX CHEN
        Senior Software Engineer
        Email: alex.chen@email.com | Phone: (555) 123-4567
        
        PROFESSIONAL SUMMARY
        Highly skilled Senior Software Engineer with 6+ years of experience in full-stack development,
        specializing in Python, React, and cloud technologies. Proven track record of leading
        high-performance teams and delivering scalable solutions.
        
        TECHNICAL SKILLS
        • Programming Languages: Python, JavaScript, TypeScript, Java
        • Frontend: React, Vue.js, Angular, HTML5, CSS3
        • Backend: Django, Flask, Node.js, FastAPI
        • Cloud Platforms: AWS, Azure, Google Cloud Platform
        • DevOps: Docker, Kubernetes, Jenkins, CI/CD
        • Databases: PostgreSQL, MongoDB, Redis
        • Machine Learning: TensorFlow, PyTorch, Scikit-learn
        
        PROFESSIONAL EXPERIENCE
        Senior Software Engineer | TechCorp Inc. | 2021 - Present
        • Led development of microservices architecture serving 10M+ users
        • Implemented machine learning models for recommendation system
        • Mentored team of 5 junior developers
        """,
        "include_market_intelligence": True
    }
    
    try:
        response = requests.post(url, json=data, timeout=30)
        if response.status_code == 200:
            print("✅ Neural Talent Analysis: SUCCESS")
            result = response.json()
            print(f"   📊 Neural Score: {result.get('neural_profile', {}).get('overall_score', 'N/A')}")
            print(f"   🎯 Hiring Recommendation: {result.get('hiring_recommendation', {}).get('decision', 'N/A')}")
        else:
            print(f"❌ Neural Talent Analysis: FAILED ({response.status_code})")
            print(f"   Error: {response.text}")
    except Exception as e:
        print(f"❌ Neural Talent Analysis: ERROR - {str(e)}")

def test_psychology_endpoint():
    """Test the quantum psychology analysis endpoint"""
    print("\n🔮 Testing Quantum Psychology Analysis Endpoint...")
    
    url = "http://localhost:8000/api/quantum/v1/psychology-analysis"
    data = {
        "employee_data": {
            "employee_id": "QE001",
            "name": "John Smith",
            "department": "Engineering",
            "position": "Senior Developer",
            "tenure_years": 3.5,
            "last_review_score": 4.2
        },
        "feedback_text": """
        I'm really enjoying the challenging projects and collaborative team environment. 
        The learning opportunities are excellent, and I feel like I'm growing professionally. 
        However, the workload has been quite intense lately, and I'm feeling a bit overwhelmed 
        with the current project deadlines. I'd appreciate more clarity on career advancement 
        opportunities and would like to discuss potential leadership roles in the future.
        """,
        "include_neurological_patterns": True,
        "behavioral_prediction_horizon": 12
    }
    
    try:
        response = requests.post(url, json=data, timeout=30)
        if response.status_code == 200:
            print("✅ Quantum Psychology Analysis: SUCCESS")
            result = response.json()
            print(f"   🔮 Engagement Score: {result.get('quantum_psychological_matrix', {}).get('engagement_metrics', {}).get('quantum_level', 'N/A')}")
            print(f"   ⚠️  Attrition Risk: {result.get('temporal_risk_assessment', {}).get('3_month_risk', 'N/A')}")
        else:
            print(f"❌ Quantum Psychology Analysis: FAILED ({response.status_code})")
            print(f"   Error: {response.text}")
    except Exception as e:
        print(f"❌ Quantum Psychology Analysis: ERROR - {str(e)}")

def test_batch_analysis_endpoint():
    """Test the batch analysis endpoint"""
    print("\n📊 Testing Batch Analysis Endpoint...")
    
    url = "http://localhost:8000/api/quantum/v1/batch-psychology-analysis"
    data = {
        "employees": [
            {
                "employee_id": "E001",
                "name": "Alice Johnson",
                "department": "Engineering",
                "position": "Software Engineer",
                "tenure_years": 2.0,
                "last_review_score": 4.5,
                "feedback": "Great team collaboration and technical skills."
            },
            {
                "employee_id": "E002", 
                "name": "Bob Wilson",
                "department": "Product",
                "position": "Product Manager",
                "tenure_years": 1.5,
                "last_review_score": 3.8,
                "feedback": "Shows leadership potential but needs more strategic thinking."
            }
        ],
        "analysis_type": "comprehensive"
    }
    
    try:
        response = requests.post(url, json=data, timeout=30)
        if response.status_code == 200:
            print("✅ Batch Analysis: SUCCESS")
            result = response.json()
            print(f"   📊 Employees Processed: {result.get('batch_summary', {}).get('total_employees', 'N/A')}")
            print(f"   ⚠️  High Risk Count: {result.get('batch_summary', {}).get('high_risk_employees', 'N/A')}")
        else:
            print(f"❌ Batch Analysis: FAILED ({response.status_code})")
            print(f"   Error: {response.text}")
    except Exception as e:
        print(f"❌ Batch Analysis: ERROR - {str(e)}")

def main():
    print("🚀 QUANTUM HR API QUICK TEST SUITE")
    print("=" * 50)
    
    # Test health endpoint first
    try:
        response = requests.get("http://localhost:8000/health", timeout=10)
        if response.status_code == 200:
            print("✅ API Health Check: PASSED")
        else:
            print("❌ API Health Check: FAILED")
            return
    except:
        print("❌ API Server not responding")
        return
    
    # Test main endpoints
    test_neural_talent_endpoint()
    test_psychology_endpoint()
    test_batch_analysis_endpoint()
    
    print("\n🏁 Test Complete!")

if __name__ == "__main__":
    main()
