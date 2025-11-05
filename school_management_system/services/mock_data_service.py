import datetime
from typing import Dict, List, Any, Optional

from school_management_system.models.user import Role
from school_management_system.models.student import EngineeringBranch, AcademicYear
from school_management_system.models.admission import AdmissionStatus
from school_management_system.models.exam import ExamType
from school_management_system.models.payment import PaymentStatus, PaymentMethod, FeeType
from school_management_system.models.report import ReportType
from school_management_system.models.timetable import DayOfWeek


class MockDataService:
    """
    Service for providing mock data for testing without a database connection.
    """
    
    @staticmethod
    def get_mock_users() -> List[Dict[str, Any]]:
        """
        Get mock user data.
        """
        return [
            {
                "id": 1,
                "email": "admin@example.com",
                "full_name": "Admin User",
                "is_active": True,
                "is_superuser": True,
                "role": "admin",
                "hashed_password": "$2b$12$EixZaYVK1fsbw1ZfbX3OXePaWxn96p36WQoeG6Lruj3vjPGga31lW",  # "password"
            },
            {
                "id": 2,
                "email": "teacher@example.com",
                "full_name": "Professor Smith",
                "is_active": True,
                "is_superuser": False,
                "role": "teacher",
                "hashed_password": "$2b$12$EixZaYVK1fsbw1ZfbX3OXePaWxn96p36WQoeG6Lruj3vjPGga31lW",  # "password"
            },
            {
                "id": 3,
                "email": "parent@example.com",
                "full_name": "Parent User",
                "is_active": True,
                "is_superuser": False,
                "role": "parent",
                "hashed_password": "$2b$12$EixZaYVK1fsbw1ZfbX3OXePaWxn96p36WQoeG6Lruj3vjPGga31lW",  # "password"
            },
        ]
    
    @staticmethod
    def get_mock_students() -> List[Dict[str, Any]]:
        """
        Get mock student data for engineering college.
        """
        return [
            {
                "id": 1,
                "first_name": "Sahana",
                "last_name": "Patel",
                "date_of_birth": datetime.date(2003, 5, 15),
                "gender": "Female",
                "enrollment_date": datetime.date(2023, 8, 1),
                "academic_year": AcademicYear.SECOND_YEAR,
                "branch": EngineeringBranch.CSE,
                "student_id": "CSE2023001",
                "address": "123 College Road, Bangalore",
                "phone_number": "9876543210",
                "email": "sahana.patel@example.com",
                "is_active": True,
                "parent_id": 3,
                "cgpa": 8.7,
                "backlogs": 0,
                "internship_company": "TechSolutions Inc.",
                "internship_status": "Ongoing",
                "project_title": "AI-based Attendance System",
                "project_guide": "Dr. Sharma",
                "placement_status": None,
                "placement_company": None,
                "scholarship_status": True,
                "scholarship_details": "Merit Scholarship - 50% tuition waiver",
                "hostel_resident": True,
                "hostel_room_number": "G-204",
            },
            {
                "id": 2,
                "first_name": "Rahul",
                "last_name": "Kumar",
                "date_of_birth": datetime.date(2002, 8, 22),
                "gender": "Male",
                "enrollment_date": datetime.date(2022, 8, 1),
                "academic_year": AcademicYear.THIRD_YEAR,
                "branch": EngineeringBranch.ECE,
                "student_id": "ECE2022042",
                "address": "456 Engineering Avenue, Chennai",
                "phone_number": "8765432109",
                "email": "rahul.kumar@example.com",
                "is_active": True,
                "parent_id": None,
                "cgpa": 9.2,
                "backlogs": 0,
                "internship_company": "ElectroTech Ltd.",
                "internship_status": "Completed",
                "project_title": "IoT-based Smart Home System",
                "project_guide": "Prof. Verma",
                "placement_status": "Placed",
                "placement_company": "Qualcomm",
                "scholarship_status": True,
                "scholarship_details": "Academic Excellence Scholarship",
                "hostel_resident": True,
                "hostel_room_number": "B-108",
            },
            {
                "id": 3,
                "first_name": "Priya",
                "last_name": "Singh",
                "date_of_birth": datetime.date(2004, 3, 10),
                "gender": "Female",
                "enrollment_date": datetime.date(2023, 8, 1),
                "academic_year": AcademicYear.FIRST_YEAR,
                "branch": EngineeringBranch.IT,
                "student_id": "IT2023015",
                "address": "789 Tech Park, Hyderabad",
                "phone_number": "7654321098",
                "email": "priya.singh@example.com",
                "is_active": True,
                "parent_id": None,
                "cgpa": 8.5,
                "backlogs": 1,
                "internship_company": None,
                "internship_status": "Not Started",
                "project_title": "Web-based Student Management System",
                "project_guide": "Dr. Gupta",
                "placement_status": None,
                "placement_company": None,
                "scholarship_status": False,
                "scholarship_details": None,
                "hostel_resident": False,
                "hostel_room_number": None,
            },
            {
                "id": 4,
                "first_name": "Arjun",
                "last_name": "Reddy",
                "date_of_birth": datetime.date(2001, 11, 5),
                "gender": "Male",
                "enrollment_date": datetime.date(2021, 8, 1),
                "academic_year": AcademicYear.FINAL_YEAR,
                "branch": EngineeringBranch.ME,
                "student_id": "ME2021007",
                "address": "101 Engineering Block, Mumbai",
                "phone_number": "6543210987",
                "email": "arjun.reddy@example.com",
                "is_active": True,
                "parent_id": None,
                "cgpa": 7.8,
                "backlogs": 2,
                "internship_company": "AutoTech Industries",
                "internship_status": "Completed",
                "project_title": "Design and Analysis of Composite Materials",
                "project_guide": "Prof. Rao",
                "placement_status": "Not Placed",
                "placement_company": None,
                "scholarship_status": False,
                "scholarship_details": None,
                "hostel_resident": True,
                "hostel_room_number": "A-305",
            },
        ]
    
    @staticmethod
    def get_mock_admissions() -> List[Dict[str, Any]]:
        """
        Get mock admission data.
        """
        return [
            {
                "id": 1,
                "application_date": datetime.date(2023, 5, 15),
                "status": AdmissionStatus.APPROVED,
                "desired_grade_level": "First Year",
                "previous_school": "Delhi Public School",
                "previous_grade_level": "12th Standard",
                "notes": "Good academic record with 95% in PCM",
                "first_name": "Sahana",
                "last_name": "Patel",
                "date_of_birth": datetime.date(2003, 5, 15),
                "gender": "Female",
                "address": "123 College Road, Bangalore",
                "phone_number": "9876543210",
                "email": "sahana.patel@example.com",
                "parent_name": "Rajesh Patel",
                "parent_phone": "9876543211",
                "parent_email": "rajesh.patel@example.com",
                "parent_address": "123 College Road, Bangalore",
                "relationship_to_applicant": "Father",
                "student_id": 1,
            },
            {
                "id": 2,
                "application_date": datetime.date(2022, 5, 20),
                "status": AdmissionStatus.APPROVED,
                "desired_grade_level": "First Year",
                "previous_school": "Chennai Public School",
                "previous_grade_level": "12th Standard",
                "notes": "Good academic record with 92% in PCM",
                "first_name": "Rahul",
                "last_name": "Kumar",
                "date_of_birth": datetime.date(2002, 8, 22),
                "gender": "Male",
                "address": "456 Engineering Avenue, Chennai",
                "phone_number": "8765432109",
                "email": "rahul.kumar@example.com",
                "parent_name": "Suresh Kumar",
                "parent_phone": "8765432100",
                "parent_email": "suresh.kumar@example.com",
                "parent_address": "456 Engineering Avenue, Chennai",
                "relationship_to_applicant": "Father",
                "student_id": 2,
            },
        ]
    
    @staticmethod
    def get_mock_subjects() -> List[Dict[str, Any]]:
        """
        Get mock subject data for engineering college.
        """
        return [
            {
                "id": 1,
                "name": "Data Structures and Algorithms",
                "code": "CS201",
                "description": "Fundamental data structures and algorithms",
                "grade_level": "Second Year",
                "credits": 4,
                "is_active": True,
                "teacher_id": 2,
            },
            {
                "id": 2,
                "name": "Database Management Systems",
                "code": "CS202",
                "description": "Principles of database design and management",
                "grade_level": "Second Year",
                "credits": 4,
                "is_active": True,
                "teacher_id": 2,
            },
            {
                "id": 3,
                "name": "Object-Oriented Programming",
                "code": "CS203",
                "description": "Concepts of object-oriented programming using Java",
                "grade_level": "Second Year",
                "credits": 3,
                "is_active": True,
                "teacher_id": 2,
            },
            {
                "id": 4,
                "name": "Digital Electronics",
                "code": "EC201",
                "description": "Fundamentals of digital electronics and logic design",
                "grade_level": "Second Year",
                "credits": 4,
                "is_active": True,
                "teacher_id": 2,
            },
            {
                "id": 5,
                "name": "Signals and Systems",
                "code": "EC202",
                "description": "Analysis of signals and systems",
                "grade_level": "Third Year",
                "credits": 4,
                "is_active": True,
                "teacher_id": 2,
            },
        ]
    
    @staticmethod
    def get_mock_timetables() -> List[Dict[str, Any]]:
        """
        Get mock timetable data.
        """
        return [
            {
                "id": 1,
                "name": "CSE Second Year Timetable",
                "description": "Timetable for CSE Second Year students",
                "academic_year": "2023-2024",
                "term": "Fall",
                "grade_level": "Second Year",
                "section": "A",
                "is_active": True,
            },
            {
                "id": 2,
                "name": "ECE Third Year Timetable",
                "description": "Timetable for ECE Third Year students",
                "academic_year": "2023-2024",
                "term": "Fall",
                "grade_level": "Third Year",
                "section": "A",
                "is_active": True,
            },
        ]
    
    @staticmethod
    def get_mock_timetable_slots() -> List[Dict[str, Any]]:
        """
        Get mock timetable slot data.
        """
        return [
            {
                "id": 1,
                "day": DayOfWeek.MONDAY,
                "start_time": datetime.time(9, 0),
                "end_time": datetime.time(10, 30),
                "room_number": "CS-101",
                "timetable_id": 1,
                "subject_id": 1,
                "teacher_id": 2,
            },
            {
                "id": 2,
                "day": DayOfWeek.MONDAY,
                "start_time": datetime.time(10, 45),
                "end_time": datetime.time(12, 15),
                "room_number": "CS-102",
                "timetable_id": 1,
                "subject_id": 2,
                "teacher_id": 2,
            },
            {
                "id": 3,
                "day": DayOfWeek.TUESDAY,
                "start_time": datetime.time(9, 0),
                "end_time": datetime.time(10, 30),
                "room_number": "CS-103",
                "timetable_id": 1,
                "subject_id": 3,
                "teacher_id": 2,
            },
            {
                "id": 4,
                "day": DayOfWeek.MONDAY,
                "start_time": datetime.time(9, 0),
                "end_time": datetime.time(10, 30),
                "room_number": "EC-101",
                "timetable_id": 2,
                "subject_id": 4,
                "teacher_id": 2,
            },
            {
                "id": 5,
                "day": DayOfWeek.MONDAY,
                "start_time": datetime.time(10, 45),
                "end_time": datetime.time(12, 15),
                "room_number": "EC-102",
                "timetable_id": 2,
                "subject_id": 5,
                "teacher_id": 2,
            },
        ]
    
    @staticmethod
    def get_mock_exams() -> List[Dict[str, Any]]:
        """
        Get mock exam data.
        """
        return [
            {
                "id": 1,
                "name": "Data Structures and Algorithms Mid-Semester",
                "description": "Mid-semester exam for Data Structures and Algorithms",
                "exam_type": ExamType.MIDTERM,
                "date": datetime.date(2023, 10, 15),
                "start_time": "09:00",
                "end_time": "12:00",
                "total_marks": 100.0,
                "passing_marks": 40.0,
                "grade_level": "Second Year",
                "academic_year": "2023-2024",
                "term": "Fall",
                "instructions": "Answer all questions. No electronic devices allowed.",
            },
            {
                "id": 2,
                "name": "Database Management Systems Mid-Semester",
                "description": "Mid-semester exam for Database Management Systems",
                "exam_type": ExamType.MIDTERM,
                "date": datetime.date(2023, 10, 17),
                "start_time": "09:00",
                "end_time": "12:00",
                "total_marks": 100.0,
                "passing_marks": 40.0,
                "grade_level": "Second Year",
                "academic_year": "2023-2024",
                "term": "Fall",
                "instructions": "Answer all questions. No electronic devices allowed.",
            },
            {
                "id": 3,
                "name": "Digital Electronics Mid-Semester",
                "description": "Mid-semester exam for Digital Electronics",
                "exam_type": ExamType.MIDTERM,
                "date": datetime.date(2023, 10, 16),
                "start_time": "09:00",
                "end_time": "12:00",
                "total_marks": 100.0,
                "passing_marks": 40.0,
                "grade_level": "Third Year",
                "academic_year": "2023-2024",
                "term": "Fall",
                "instructions": "Answer all questions. No electronic devices allowed.",
            },
        ]
    
    @staticmethod
    def get_mock_exam_results() -> List[Dict[str, Any]]:
        """
        Get mock exam result data.
        """
        return [
            {
                "id": 1,
                "score": 85.0,
                "grade": "A",
                "remarks": "Excellent understanding of concepts",
                "student_id": 1,
                "exam_id": 1,
                "subject_id": 1,
            },
            {
                "id": 2,
                "score": 78.0,
                "grade": "B",
                "remarks": "Good performance, needs improvement in normalization",
                "student_id": 1,
                "exam_id": 2,
                "subject_id": 2,
            },
            {
                "id": 3,
                "score": 92.0,
                "grade": "A+",
                "remarks": "Outstanding performance",
                "student_id": 2,
                "exam_id": 3,
                "subject_id": 4,
            },
        ]
    
    @staticmethod
    def get_mock_fee_structures() -> List[Dict[str, Any]]:
        """
        Get mock fee structure data.
        """
        return [
            {
                "id": 1,
                "name": "CSE Department Fee Structure",
                "description": "Fee structure for Computer Science and Engineering students",
                "academic_year": "2023-2024",
                "grade_level": "All",
                "is_active": True,
            },
            {
                "id": 2,
                "name": "ECE Department Fee Structure",
                "description": "Fee structure for Electronics and Communication Engineering students",
                "academic_year": "2023-2024",
                "grade_level": "All",
                "is_active": True,
            },
        ]
    
    @staticmethod
    def get_mock_fee_items() -> List[Dict[str, Any]]:
        """
        Get mock fee item data.
        """
        return [
            {
                "id": 1,
                "name": "Tuition Fee",
                "description": "Tuition fee for the academic year",
                "fee_type": FeeType.TUITION,
                "amount": 85000.0,
                "due_date": datetime.date(2023, 8, 15),
                "is_mandatory": True,
                "fee_structure_id": 1,
            },
            {
                "id": 2,
                "name": "Laboratory Fee",
                "description": "Laboratory fee for the academic year",
                "fee_type": FeeType.LABORATORY,
                "amount": 15000.0,
                "due_date": datetime.date(2023, 8, 15),
                "is_mandatory": True,
                "fee_structure_id": 1,
            },
            {
                "id": 3,
                "name": "Hostel Fee",
                "description": "Hostel fee for the academic year",
                "fee_type": FeeType.HOSTEL,
                "amount": 60000.0,
                "due_date": datetime.date(2023, 8, 15),
                "is_mandatory": False,
                "fee_structure_id": 1,
            },
            {
                "id": 4,
                "name": "Tuition Fee",
                "description": "Tuition fee for the academic year",
                "fee_type": FeeType.TUITION,
                "amount": 80000.0,
                "due_date": datetime.date(2023, 8, 15),
                "is_mandatory": True,
                "fee_structure_id": 2,
            },
            {
                "id": 5,
                "name": "Laboratory Fee",
                "description": "Laboratory fee for the academic year",
                "fee_type": FeeType.LABORATORY,
                "amount": 20000.0,
                "due_date": datetime.date(2023, 8, 15),
                "is_mandatory": True,
                "fee_structure_id": 2,
            },
        ]
    
    @staticmethod
    def get_mock_fee_records() -> List[Dict[str, Any]]:
        """
        Get mock fee record data.
        """
        return [
            {
                "id": 1,
                "academic_year": "2023-2024",
                "term": "Fall",
                "total_amount": 100000.0,
                "paid_amount": 50000.0,
                "balance": 50000.0,
                "status": PaymentStatus.PARTIALLY_PAID,
                "due_date": datetime.date(2023, 8, 15),
                "student_id": 1,
                "fee_structure_id": 1,
            },
            {
                "id": 2,
                "academic_year": "2023-2024",
                "term": "Fall",
                "total_amount": 100000.0,
                "paid_amount": 100000.0,
                "balance": 0.0,
                "status": PaymentStatus.PAID,
                "due_date": datetime.date(2023, 8, 15),
                "student_id": 2,
                "fee_structure_id": 2,
            },
        ]
    
    @staticmethod
    def get_mock_payments() -> List[Dict[str, Any]]:
        """
        Get mock payment data.
        """
        return [
            {
                "id": 1,
                "amount": 50000.0,
                "payment_date": datetime.datetime(2023, 8, 10, 10, 0),
                "payment_method": PaymentMethod.BANK_TRANSFER,
                "transaction_id": "TXN123456",
                "receipt_number": "REC123456",
                "notes": "First installment",
                "fee_record_id": 1,
            },
            {
                "id": 2,
                "amount": 100000.0,
                "payment_date": datetime.datetime(2023, 8, 5, 11, 0),
                "payment_method": PaymentMethod.BANK_TRANSFER,
                "transaction_id": "TXN123457",
                "receipt_number": "REC123457",
                "notes": "Full payment",
                "fee_record_id": 2,
            },
        ]
    
    @staticmethod
    def get_mock_reports() -> List[Dict[str, Any]]:
        """
        Get mock report data.
        """
        return [
            {
                "id": 1,
                "title": "Attendance Report",
                "description": "Monthly attendance report for all departments",
                "report_type": ReportType.ATTENDANCE,
                "created_at": datetime.datetime(2023, 10, 1, 9, 0),
                "created_by": 1,
                "parameters": '{"month": "September", "year": "2023"}',
                "file_path": "/reports/attendance_report_202309.pdf",
                "is_scheduled": True,
                "schedule_frequency": "Monthly",
                "last_run": datetime.datetime(2023, 10, 1, 9, 0),
                "next_run": datetime.datetime(2023, 11, 1, 9, 0),
            },
            {
                "id": 2,
                "title": "Academic Performance Report",
                "description": "Mid-semester academic performance report",
                "report_type": ReportType.ACADEMIC,
                "created_at": datetime.datetime(2023, 10, 20, 10, 0),
                "created_by": 1,
                "parameters": '{"term": "Fall", "year": "2023"}',
                "file_path": "/reports/academic_report_2023_fall.pdf",
                "is_scheduled": False,
                "schedule_frequency": None,
                "last_run": datetime.datetime(2023, 10, 20, 10, 0),
                "next_run": None,
            },
            {
                "id": 3,
                "title": "Placement Statistics Report",
                "description": "Annual placement statistics report",
                "report_type": ReportType.CUSTOM,
                "created_at": datetime.datetime(2023, 9, 15, 14, 0),
                "created_by": 1,
                "parameters": '{"year": "2023"}',
                "file_path": "/reports/placement_statistics_2023.pdf",
                "is_scheduled": True,
                "schedule_frequency": "Yearly",
                "last_run": datetime.datetime(2023, 9, 15, 14, 0),
                "next_run": datetime.datetime(2024, 9, 15, 14, 0),
            },
        ]
    
    @classmethod
    def get_mock_data(cls, model_name: str) -> List[Dict[str, Any]]:
        """
        Get mock data for a specific model.
        """
        mock_data_methods = {
            "users": cls.get_mock_users,
            "students": cls.get_mock_students,
            "admissions": cls.get_mock_admissions,
            "subjects": cls.get_mock_subjects,
            "timetables": cls.get_mock_timetables,
            "timetable_slots": cls.get_mock_timetable_slots,
            "exams": cls.get_mock_exams,
            "exam_results": cls.get_mock_exam_results,
            "fee_structures": cls.get_mock_fee_structures,
            "fee_items": cls.get_mock_fee_items,
            "fee_records": cls.get_mock_fee_records,
            "payments": cls.get_mock_payments,
            "reports": cls.get_mock_reports,
        }
        
        if model_name in mock_data_methods:
            return mock_data_methods[model_name]()
        
        return []
    
    @classmethod
    def get_mock_item_by_id(cls, model_name: str, item_id: int) -> Optional[Dict[str, Any]]:
        """
        Get a mock item by ID.
        """
        items = cls.get_mock_data(model_name)
        for item in items:
            if item["id"] == item_id:
                return item
        
        return None
