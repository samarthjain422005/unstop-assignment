"""
🚀 HR-Tech Quantum Innovation Challenge: Comprehensive API Testing Script
Revolutionary API testing and validation for the Quantum Workforce Intelligence Platform
"""

import requests
import json
import time
from datetime import datetime
import pandas as pd

class QuantumAPITester:
    def __init__(self, base_url="http://localhost:8000"):
        self.base_url = base_url
        self.test_results = []
        
    def test_health_endpoint(self):
        """Test the API health endpoint"""
        print("🔍 Testing API Health Endpoint...")
        try:
            response = requests.get(f"{self.base_url}/health", timeout=10)
            if response.status_code == 200:
                print("✅ API Health Check: PASSED")
                return True
            else:
                print(f"❌ API Health Check: FAILED (Status: {response.status_code})")
                return False
        except requests.RequestException as e:
            print(f"❌ API Health Check: FAILED (Error: {str(e)})")
            return False
    
    def test_neural_talent_analysis_api(self):
        """Test Neural Talent Acquisition Intelligence API"""
        print("\n🧬 Testing Neural Talent Acquisition Intelligence API...")
          # Sample resume data for testing
        test_data = {
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
            start_time = time.time()
            response = requests.post(
                f"{self.base_url}/api/quantum/v1/neural-talent-analysis",
                json=test_data,
                timeout=30
            )
            processing_time = time.time() - start_time
            
            if response.status_code == 200:
                result = response.json()
                print("✅ Neural Talent Analysis API: PASSED")
                print(f"⚡ Processing Time: {processing_time:.2f} seconds")
                print(f"🎯 Neural Match Score: {result.get('neural_match_score', 'N/A')}")
                print(f"🧬 Behavioral DNA Score: {result.get('behavioral_dna_analysis', {}).get('overall_score', 'N/A')}")
                print(f"📊 Market Intelligence Score: {result.get('market_intelligence', {}).get('competitive_positioning', 'N/A')}")
                return True, result
            else:
                print(f"❌ Neural Talent Analysis API: FAILED (Status: {response.status_code})")
                print(f"Error: {response.text}")
                return False, None
                  except requests.RequestException as e:
            print(f"❌ Neural Talent Analysis API: FAILED (Error: {str(e)})")
            return False, None
    
    def test_quantum_psychology_api(self):
        """Test Quantum Employee Psychology Analytics API"""
        print("\n🔮 Testing Quantum Employee Psychology Analytics API...")
        
        test_data = {
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
            start_time = time.time()
            response = requests.post(
                f"{self.base_url}/api/quantum/v1/psychology-analysis",
                json=test_data,
                timeout=30
            )
            processing_time = time.time() - start_time
            
            if response.status_code == 200:
                result = response.json()
                print("✅ Quantum Psychology Analysis API: PASSED")
                print(f"⚡ Processing Time: {processing_time:.2f} seconds")
                print(f"🔮 Quantum Engagement Score: {result.get('quantum_engagement_score', 'N/A')}")
                print(f"⚠️  Attrition Risk (6 months): {result.get('temporal_attrition_forecast', {}).get('6_months', 'N/A')}%")
                print(f"💡 Intervention Priority: {result.get('intervention_strategy', {}).get('priority_level', 'N/A')}")
                return True, result
            else:
                print(f"❌ Quantum Psychology Analysis API: FAILED (Status: {response.status_code})")
                print(f"Error: {response.text}")
                return False, None
                
        except requests.RequestException as e:
            print(f"❌ Quantum Psychology Analysis API: FAILED (Error: {str(e)})")
            return False, None
    
    def test_batch_analysis_api(self):
        """Test Batch Analysis API for multiple employees"""
        print("\n📊 Testing Batch Analysis API...")
        
        # Load sample employee data
        try:
            employees_df = pd.read_csv("sample_data/quantum_employees.csv")
            sample_employees = employees_df.head(5).to_dict('records')
            
            test_data = {
                "employees": [
                    {
                        "employee_id": emp["employee_id"],
                        "employee_metadata": {
                            "name": emp["name"],
                            "department": emp["department"],
                            "position": emp["position"],
                            "tenure_years": emp["tenure_years"]
                        },
                        "feedback_text": emp["feedback_text"]
                    }
                    for emp in sample_employees
                ]
            }
            
            start_time = time.time()
            response = requests.post(
                f"{self.base_url}/api/quantum/v1/batch-psychology-analysis",
                json=test_data,
                timeout=60
            )
            processing_time = time.time() - start_time
            
            if response.status_code == 200:
                result = response.json()
                print("✅ Batch Analysis API: PASSED")
                print(f"⚡ Processing Time: {processing_time:.2f} seconds")
                print(f"📊 Employees Processed: {len(result.get('results', []))}")
                print(f"🎯 Average Processing Time per Employee: {processing_time/len(sample_employees):.2f} seconds")
                return True, result
            else:
                print(f"❌ Batch Analysis API: FAILED (Status: {response.status_code})")
                print(f"Error: {response.text}")
                return False, None
                
        except Exception as e:
            print(f"❌ Batch Analysis API: FAILED (Error: {str(e)})")
            return False, None
    
    def test_ceo_dashboard_api(self):
        """Test CEO Quantum Dashboard API"""
        print("\n🏆 Testing CEO Quantum Dashboard API...")
        
        try:
            start_time = time.time()
            response = requests.get(
                f"{self.base_url}/api/quantum/v1/ceo-dashboard",
                timeout=30
            )
            processing_time = time.time() - start_time
            
            if response.status_code == 200:
                result = response.json()
                print("✅ CEO Quantum Dashboard API: PASSED")
                print(f"⚡ Processing Time: {processing_time:.2f} seconds")
                print(f"📊 Workforce Health Score: {result.get('workforce_health_score', 'N/A')}")
                print(f"⚠️  High-Risk Employees: {result.get('high_risk_employees', 'N/A')}")
                print(f"🎯 Top Performer Percentage: {result.get('top_performer_percentage', 'N/A')}%")
                return True, result
            else:
                print(f"❌ CEO Quantum Dashboard API: FAILED (Status: {response.status_code})")
                print(f"Error: {response.text}")
                return False, None
                
        except requests.RequestException as e:
            print(f"❌ CEO Quantum Dashboard API: FAILED (Error: {str(e)})")
            return False, None
    
    def run_comprehensive_tests(self):
        """Run all API tests and generate a comprehensive report"""
        print("🚀 QUANTUM API COMPREHENSIVE TESTING SUITE")
        print("=" * 60)
        print(f"🕒 Test Started: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"🌐 Base URL: {self.base_url}")
        
        results = {
            'health_check': False,
            'neural_talent_analysis': False,
            'quantum_psychology_analysis': False,
            'batch_analysis': False,
            'ceo_dashboard': False,
            'total_tests': 5,
            'passed_tests': 0,
            'start_time': datetime.now()
        }
        
        # Test 1: Health Check
        results['health_check'] = self.test_health_endpoint()
        if results['health_check']:
            results['passed_tests'] += 1
        
        # Test 2: Neural Talent Analysis
        success, _ = self.test_neural_talent_analysis_api()
        results['neural_talent_analysis'] = success
        if success:
            results['passed_tests'] += 1
        
        # Test 3: Quantum Psychology Analysis
        success, _ = self.test_quantum_psychology_api()
        results['quantum_psychology_analysis'] = success
        if success:
            results['passed_tests'] += 1
        
        # Test 4: Batch Analysis
        success, _ = self.test_batch_analysis_api()
        results['batch_analysis'] = success
        if success:
            results['passed_tests'] += 1
        
        # Test 5: CEO Dashboard
        success, _ = self.test_ceo_dashboard_api()
        results['ceo_dashboard'] = success
        if success:
            results['passed_tests'] += 1
        
        # Generate test report
        self.generate_test_report(results)
        
        return results
    
    def generate_test_report(self, results):
        """Generate comprehensive test report"""
        print("\n" + "=" * 60)
        print("📊 QUANTUM API TEST RESULTS SUMMARY")
        print("=" * 60)
        
        success_rate = (results['passed_tests'] / results['total_tests']) * 100
        
        print(f"✅ Tests Passed: {results['passed_tests']}/{results['total_tests']}")
        print(f"📈 Success Rate: {success_rate:.1f}%")
        print(f"🕒 Test Duration: {datetime.now() - results['start_time']}")
        
        print("\n🔍 INDIVIDUAL TEST RESULTS:")
        test_status = {
            'health_check': '🟢 Health Check',
            'neural_talent_analysis': '🧬 Neural Talent Analysis',
            'quantum_psychology_analysis': '🔮 Quantum Psychology Analysis',
            'batch_analysis': '📊 Batch Analysis',
            'ceo_dashboard': '🏆 CEO Dashboard'
        }
        
        for test_key, test_name in test_status.items():
            status = "✅ PASSED" if results[test_key] else "❌ FAILED"
            print(f"   {test_name}: {status}")
        
        print("\n🎯 RECOMMENDATIONS:")
        if success_rate == 100:
            print("   🏆 All tests passed! API is ready for production deployment.")
        elif success_rate >= 80:
            print("   🚀 Most tests passed. Minor issues may need attention.")
        elif success_rate >= 60:
            print("   ⚠️  Some critical issues detected. Review failed tests.")
        else:
            print("   🚨 Major issues detected. API requires immediate attention.")
        
        # Save test report to file
        report_data = {
            'test_timestamp': datetime.now().isoformat(),
            'success_rate': success_rate,
            'results': results,
            'base_url': self.base_url
        }
        
        with open('api_test_report.json', 'w') as f:
            json.dump(report_data, f, indent=2, default=str)
        
        print(f"\n📄 Detailed test report saved to: api_test_report.json")

def main():
    """Main function to run API tests"""
    print("🔮 Initializing Quantum API Testing Suite...")
    
    # Check if API server is running
    tester = QuantumAPITester()
    
    # Wait a moment for server to be ready
    print("⏳ Waiting for API server to be ready...")
    time.sleep(3)
    
    # Run comprehensive tests
    results = tester.run_comprehensive_tests()
    
    return results

if __name__ == "__main__":
    main()
