"""
🔮 HR-Tech Quantum Innovation Challenge: Comprehensive Sample Data G            # Generate scores with realistic correlations
            base_score = np.random.normal(80, 12)
            neural_match_score = max(60, min(100, base_score + np.random.normal(0, 5)))
            behavioral_dna_score = max(60, min(100, base_score + np.random.normal(0, 8)))
            market_intelligence_score = max(60, min(100, base_score + np.random.normal(0, 6)))ator
Revolutionary sample data creation for testing and demonstration purposes
"""

import pandas as pd
import numpy as np
import json
import os
from datetime import datetime, timedelta
import random

class QuantumSampleDataGenerator:
    def __init__(self):
        self.departments = ['Engineering', 'Marketing', 'Sales', 'HR', 'Finance', 'Operations', 'Design', 'Product']
        self.positions = {
            'Engineering': ['Software Engineer', 'Senior Software Engineer', 'Lead Engineer', 'Engineering Manager', 'DevOps Engineer', 'Data Scientist'],
            'Marketing': ['Marketing Manager', 'Content Specialist', 'Digital Marketing Lead', 'Brand Manager', 'Growth Hacker'],
            'Sales': ['Sales Representative', 'Account Manager', 'Sales Director', 'Business Development', 'Sales Engineer'],
            'HR': ['HR Generalist', 'Talent Acquisition', 'HR Business Partner', 'Learning & Development', 'Compensation Analyst'],
            'Finance': ['Financial Analyst', 'Accountant', 'Finance Manager', 'Budget Analyst', 'Controller'],
            'Operations': ['Operations Manager', 'Process Analyst', 'Supply Chain Manager', 'Quality Assurance'],
            'Design': ['UX Designer', 'UI Designer', 'Product Designer', 'Design Lead', 'Visual Designer'],
            'Product': ['Product Manager', 'Product Owner', 'Product Analyst', 'Product Marketing Manager']
        }
        
        self.skills_database = {
            'Programming': ['Python', 'JavaScript', 'Java', 'C++', 'React', 'Angular', 'Vue.js', 'Node.js', 'Django', 'Flask'],
            'Cloud': ['AWS', 'Azure', 'Google Cloud', 'Kubernetes', 'Docker', 'Terraform', 'Jenkins'],
            'Data': ['SQL', 'PostgreSQL', 'MongoDB', 'Redis', 'Elasticsearch', 'Pandas', 'NumPy', 'TensorFlow', 'PyTorch'],
            'DevOps': ['Git', 'CI/CD', 'Linux', 'Bash', 'Monitoring', 'Security', 'Microservices'],
            'Soft Skills': ['Leadership', 'Communication', 'Problem Solving', 'Teamwork', 'Adaptability', 'Innovation']
        }
        
        self.psychological_traits = ['Openness', 'Conscientiousness', 'Extraversion', 'Agreeableness', 'Neuroticism']
        
        self.feedback_templates = [
            "I'm really enjoying the challenging projects and collaborative team environment. The learning opportunities are excellent.",
            "The workload has been quite intense lately, and I'm feeling a bit overwhelmed with the current project deadlines.",
            "I appreciate the flexibility in work arrangements, but I'd like more clarity on career advancement opportunities.",
            "The team dynamics are fantastic, and I feel valued for my contributions. Looking forward to taking on more responsibilities.",
            "I'm concerned about the lack of professional development budget and limited training opportunities available.",
            "The company culture is great, but I'm not satisfied with the current compensation package compared to market rates.",
            "I love the innovative projects we're working on, but the communication between departments could be improved.",
            "The management is supportive, but I feel like my ideas aren't being heard in team meetings.",
            "I'm excited about the company's direction, but the remote work policy needs some adjustments for better work-life balance.",
            "The technical challenges keep me engaged, but I'm looking for more mentorship opportunities to grow my skills."
        ]
        
    def generate_candidate_profiles(self, num_candidates=50):
        """Generate realistic candidate profiles for neural talent acquisition testing"""
        candidates = []
        
        first_names = ['Alex', 'Sarah', 'Michael', 'Emily', 'David', 'Lisa', 'John', 'Maria', 'Robert', 'Jennifer',
                      'James', 'Amanda', 'Chris', 'Nicole', 'Daniel', 'Jessica', 'Matthew', 'Ashley', 'Andrew', 'Stephanie']
        last_names = ['Chen', 'Rodriguez', 'Kumar', 'Zhang', 'Johnson', 'Thompson', 'Lee', 'Garcia', 'Brown', 'Davis',
                     'Wilson', 'Martinez', 'Taylor', 'Anderson', 'Jackson', 'White', 'Harris', 'Clark', 'Lewis', 'Walker']
        
        for i in range(num_candidates):
            candidate_id = f"QC{i+1:03d}"
            first_name = random.choice(first_names)
            last_name = random.choice(last_names)
            
            # Generate experience and skills
            years_experience = np.random.normal(5, 2.5)
            years_experience = max(0.5, min(15, years_experience))
            
            # Select primary skills based on role
            primary_skills = random.sample(self.skills_database['Programming'], random.randint(3, 6))
            cloud_skills = random.sample(self.skills_database['Cloud'], random.randint(2, 4))
            data_skills = random.sample(self.skills_database['Data'], random.randint(2, 5))
            soft_skills = random.sample(self.skills_database['Soft Skills'], random.randint(3, 5))
              # Generate scores with realistic correlations
            base_score = np.random.normal(80, 12)
            neural_match_score = max(60, min(100, base_score + np.random.normal(0, 5)))
            behavioral_dna_score = max(60, min(100, base_score + np.random.normal(0, 8)))
            market_intelligence_score = max(60, min(100, base_score + np.random.normal(0, 6)))
            
            # Determine recommendation based on scores
            avg_score = (neural_match_score + behavioral_dna_score + market_intelligence_score) / 3
            if avg_score >= 90:
                recommendation = "Neural Highly Recommended"
                competitive_positioning = random.choice(["Top 5%", "Top 10%"])
            elif avg_score >= 80:
                recommendation = "Highly Recommended"
                competitive_positioning = random.choice(["Top 15%", "Top 20%", "Top 25%"])
            elif avg_score >= 70:
                recommendation = "Recommended"
                competitive_positioning = random.choice(["Top 30%", "Top 35%", "Top 40%"])
            else:
                recommendation = "Consider"
                competitive_positioning = random.choice(["Top 50%", "Average"])
            
            # Generate psychological traits
            psychological_profile = {}
            for trait in self.psychological_traits:
                psychological_profile[trait] = round(np.random.normal(75, 15), 1)
                psychological_profile[trait] = max(30, min(100, psychological_profile[trait]))
            
            candidate = {
                'candidate_id': candidate_id,
                'name': f"{first_name} {last_name}",
                'email': f"{first_name.lower()}.{last_name.lower()}@email.com",
                'years_experience': round(years_experience, 1),
                'neural_match_score': round(neural_match_score, 1),
                'behavioral_dna_score': round(behavioral_dna_score, 1),
                'market_intelligence_score': round(market_intelligence_score, 1),
                'quantum_recommendation': recommendation,
                'competitive_positioning': competitive_positioning,
                'predicted_performance': round(avg_score + np.random.normal(0, 5), 1),
                'cultural_fit_score': round(np.random.normal(80, 10), 1),
                'innovation_potential': round(np.random.normal(75, 12), 1),
                'primary_skills': primary_skills,
                'cloud_skills': cloud_skills,
                'data_skills': data_skills,
                'soft_skills': soft_skills,
                'psychological_profile': psychological_profile,
                'resume_summary': self._generate_resume_summary(first_name, last_name, years_experience, primary_skills)
            }
            
            candidates.append(candidate)
        
        return pd.DataFrame(candidates)
    
    def generate_employee_profiles(self, num_employees=100):
        """Generate realistic employee profiles for quantum psychology analytics testing"""
        employees = []
        
        first_names = ['John', 'Maria', 'Robert', 'Jennifer', 'James', 'Amanda', 'Chris', 'Nicole', 'Daniel', 'Jessica',
                      'Matthew', 'Ashley', 'Andrew', 'Stephanie', 'Kevin', 'Michelle', 'Brian', 'Melissa', 'Steven', 'Angela']
        last_names = ['Smith', 'Garcia', 'Lee', 'Brown', 'Wilson', 'Davis', 'Taylor', 'Martinez', 'Anderson', 'Jackson',
                     'White', 'Harris', 'Clark', 'Lewis', 'Walker', 'Young', 'Allen', 'King', 'Wright', 'Scott']
        
        for i in range(num_employees):
            employee_id = f"QE{i+1:03d}"
            first_name = random.choice(first_names)
            last_name = random.choice(last_names)
            department = random.choice(self.departments)
            position = random.choice(self.positions[department])
            
            # Generate tenure with realistic distribution
            tenure_years = np.random.exponential(2.5)
            tenure_years = max(0.1, min(15, tenure_years))
            
            # Generate engagement and risk scores with correlations
            base_engagement = np.random.normal(75, 15)
            quantum_engagement_score = max(30, min(100, base_engagement))
            
            # Risk scores increase over time with some variability
            attrition_risk_1_month = max(1, min(50, np.random.normal(15, 8)))
            attrition_risk_3_months = max(attrition_risk_1_month, min(60, attrition_risk_1_month + np.random.normal(10, 5)))
            attrition_risk_6_months = max(attrition_risk_3_months, min(75, attrition_risk_3_months + np.random.normal(15, 8)))
            attrition_risk_12_months = max(attrition_risk_6_months, min(90, attrition_risk_6_months + np.random.normal(20, 10)))
            
            # Determine psychological state and intervention priority
            if quantum_engagement_score >= 85:
                psychological_state = random.choice(['Thriving', 'Flourishing'])
                intervention_priority = 'Low'
            elif quantum_engagement_score >= 70:
                psychological_state = random.choice(['Content', 'Stable'])
                intervention_priority = 'Low'
            elif quantum_engagement_score >= 55:
                psychological_state = random.choice(['Concerned', 'Stable'])
                intervention_priority = 'Medium'
            else:
                psychological_state = random.choice(['At Risk', 'Concerned'])
                intervention_priority = 'High'
            
            # Generate intervention success prediction
            if intervention_priority == 'Low':
                predicted_intervention_success = np.random.normal(90, 8)
            elif intervention_priority == 'Medium':
                predicted_intervention_success = np.random.normal(78, 10)
            else:
                predicted_intervention_success = np.random.normal(65, 12)
            
            predicted_intervention_success = max(40, min(100, predicted_intervention_success))
            
            # Generate feedback text
            feedback_text = random.choice(self.feedback_templates)
            if intervention_priority == 'High':
                feedback_text = feedback_text.replace("enjoying", "struggling with").replace("fantastic", "challenging")
            
            employee = {
                'employee_id': employee_id,
                'name': f"{first_name} {last_name}",
                'email': f"{first_name.lower()}.{last_name.lower()}@company.com",
                'department': department,
                'position': position,
                'tenure_years': round(tenure_years, 1),
                'quantum_engagement_score': round(quantum_engagement_score, 1),
                'attrition_risk_1_month': round(attrition_risk_1_month, 1),
                'attrition_risk_3_months': round(attrition_risk_3_months, 1),
                'attrition_risk_6_months': round(attrition_risk_6_months, 1),
                'attrition_risk_12_months': round(attrition_risk_12_months, 1),
                'psychological_state': psychological_state,
                'intervention_priority': intervention_priority,
                'predicted_intervention_success': round(predicted_intervention_success, 1),
                'feedback_text': feedback_text,
                'hire_date': (datetime.now() - timedelta(days=int(tenure_years * 365))).strftime('%Y-%m-%d'),
                'last_review_date': (datetime.now() - timedelta(days=random.randint(30, 365))).strftime('%Y-%m-%d')
            }
            
            employees.append(employee)
        
        return pd.DataFrame(employees)
    
    def _generate_resume_summary(self, first_name, last_name, years_exp, skills):
        """Generate a realistic resume summary"""
        return f"""
        {first_name.upper()} {last_name.upper()}
        Senior Software Engineer
        Email: {first_name.lower()}.{last_name.lower()}@email.com
        
        PROFESSIONAL SUMMARY
        Experienced software engineer with {years_exp:.1f}+ years of experience in full-stack development.
        Specializing in {', '.join(skills[:3])}. Proven track record of delivering scalable solutions
        and leading high-performance development teams.
        
        TECHNICAL SKILLS
        • Programming: {', '.join(skills)}
        • Cloud Platforms: AWS, Azure, Google Cloud Platform
        • DevOps: Docker, Kubernetes, Jenkins, CI/CD
        • Databases: PostgreSQL, MongoDB, Redis
        
        EXPERIENCE
        Senior Software Engineer | TechCorp Inc. | 2020 - Present
        • Led development of microservices architecture serving millions of users
        • Implemented machine learning models improving system performance by 20%
        • Mentored junior developers and established coding best practices
        """
    
    def generate_market_intelligence_data(self):
        """Generate market intelligence data for competitive analysis"""
        return {
            'talent_scarcity_index': {
                'Python': 85,
                'JavaScript': 72,
                'React': 78,
                'AWS': 82,
                'Machine Learning': 91,
                'DevOps': 79,
                'Data Science': 88
            },
            'salary_benchmarks': {
                'Junior Developer': {'min': 65000, 'avg': 75000, 'max': 85000},
                'Senior Developer': {'min': 95000, 'avg': 115000, 'max': 135000},
                'Lead Engineer': {'min': 125000, 'avg': 145000, 'max': 165000},
                'Engineering Manager': {'min': 140000, 'avg': 165000, 'max': 190000}
            },
            'demand_trends': {
                'AI/ML': 'Very High',
                'Cloud Native': 'High',
                'DevOps': 'High',
                'Full Stack': 'Medium',
                'Mobile Development': 'Medium'
            }
        }
    
    def save_sample_data(self, output_dir="sample_data"):
        """Generate and save all sample data to files"""
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        
        print("🔮 Generating Quantum Sample Data...")
        
        # Generate candidate data
        candidates_df = self.generate_candidate_profiles(50)
        candidates_df.to_csv(f"{output_dir}/quantum_candidates.csv", index=False)
        print(f"✅ Generated {len(candidates_df)} candidate profiles")
        
        # Generate employee data
        employees_df = self.generate_employee_profiles(100)
        employees_df.to_csv(f"{output_dir}/quantum_employees.csv", index=False)
        print(f"✅ Generated {len(employees_df)} employee profiles")
        
        # Generate market intelligence data
        market_data = self.generate_market_intelligence_data()
        with open(f"{output_dir}/market_intelligence.json", 'w') as f:
            json.dump(market_data, f, indent=2)
        print("✅ Generated market intelligence data")
        
        # Generate summary statistics
        summary = {
            'generation_date': datetime.now().isoformat(),
            'candidates_count': len(candidates_df),
            'employees_count': len(employees_df),
            'departments': list(employees_df['department'].unique()),
            'avg_neural_match_score': float(candidates_df['neural_match_score'].mean()),
            'avg_quantum_engagement': float(employees_df['quantum_engagement_score'].mean()),
            'high_risk_employees': len(employees_df[employees_df['intervention_priority'] == 'High']),
            'top_candidates': len(candidates_df[candidates_df['neural_match_score'] >= 90])
        }
        
        with open(f"{output_dir}/data_summary.json", 'w') as f:
            json.dump(summary, f, indent=2)
        print("✅ Generated data summary")
        
        print(f"\n🚀 All sample data saved to '{output_dir}' directory!")
        return candidates_df, employees_df, market_data, summary

if __name__ == "__main__":
    generator = QuantumSampleDataGenerator()
    candidates_df, employees_df, market_data, summary = generator.save_sample_data()
    
    print("\n📊 QUANTUM SAMPLE DATA GENERATION COMPLETE!")
    print("=" * 50)
    print(f"🎯 Candidates Generated: {summary['candidates_count']}")
    print(f"🧠 Employees Generated: {summary['employees_count']}")
    print(f"🏢 Departments: {len(summary['departments'])}")
    print(f"📈 Avg Neural Match Score: {summary['avg_neural_match_score']:.1f}")
    print(f"🔮 Avg Quantum Engagement: {summary['avg_quantum_engagement']:.1f}")
    print(f"⚠️  High-Risk Employees: {summary['high_risk_employees']}")
    print(f"🏆 Top Candidates (≥90): {summary['top_candidates']}")
