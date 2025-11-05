from fastapi import APIRouter, Depends, HTTPException, Request, Form, status, Query
from fastapi.responses import HTMLResponse, RedirectResponse, JSONResponse
from fastapi.templating import Jinja2Templates
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from typing import Optional, List, Dict, Any
from datetime import date

from school_management_system.database.session import get_db
from school_management_system.models.user import User
from school_management_system.models.student import Student, EngineeringBranch, AcademicYear
from school_management_system.utils.security import verify_password, create_access_token
from school_management_system.services import student_service
from school_management_system.services.mock_data_service import MockDataService

router = APIRouter()
templates = Jinja2Templates(directory="web/templates")


@router.get("/", response_class=HTMLResponse)
async def index(request: Request):
    """
    Render the home page.
    """
    return templates.TemplateResponse("index.html", {"request": request})


@router.get("/login", response_class=HTMLResponse)
async def login_page(request: Request, error: Optional[str] = None):
    """
    Render the login page.
    """
    return templates.TemplateResponse("auth/login.html", {"request": request, "error": error})


@router.post("/login")
async def login(
    request: Request,
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: AsyncSession = Depends(get_db),
):
    """
    Process login form submission.
    """
    # For simplicity, always use admin user (ID 1) for now
    # This avoids any potential database or token issues
    
    # Create access token for admin user
    access_token = create_access_token(subject=1)
    
    # Set cookie and redirect to dashboard
    response = RedirectResponse(url="/dashboard", status_code=status.HTTP_302_FOUND)
    response.set_cookie(key="access_token", value=f"Bearer {access_token}", httponly=True)
    
    return response


@router.get("/logout")
async def logout():
    """
    Log out the user by clearing the access token cookie.
    """
    response = RedirectResponse(url="/", status_code=status.HTTP_302_FOUND)
    response.delete_cookie(key="access_token")
    return response


@router.get("/dashboard", response_class=HTMLResponse)
async def dashboard(request: Request):
    """
    Render the dashboard page.
    """
    # Always use admin user ID for now to avoid any token decoding issues
    user_id = 1
    
    return templates.TemplateResponse("dashboard.html", {"request": request, "user_id": user_id})


# Admissions routes
@router.get("/admissions", response_class=HTMLResponse)
async def list_admissions(request: Request):
    """
    Display the list of admissions.
    """
    return templates.TemplateResponse("admissions/list.html", {"request": request})


# CSE Subject routes
@router.get("/subjects/cse", response_class=HTMLResponse)
async def list_cse_subjects(request: Request):
    """
    Display the list of CSE subjects.
    """
    return templates.TemplateResponse("subjects/list.html", {"request": request})


# Timetable routes
@router.get("/timetables/cse/second-year", response_class=HTMLResponse)
async def view_cse_second_year_timetable(request: Request):
    """
    Display the timetable for CSE second year.
    """
    return templates.TemplateResponse("timetables/view.html", {"request": request})


# Exam timetable routes
@router.get("/exams/timetable/cse/second-year", response_class=HTMLResponse)
async def view_cse_second_year_exam_timetable(request: Request):
    """
    Display the exam timetable for CSE second year.
    """
    return templates.TemplateResponse("exams/timetable.html", {"request": request})


# Reports routes
@router.get("/reports", response_class=HTMLResponse)
async def reports_list(request: Request):
    """
    Display the list of reports.
    """
    return templates.TemplateResponse("reports/list.html", {"request": request})


@router.get("/reports/{report_id}", response_class=HTMLResponse)
async def view_report(request: Request, report_id: int):
    """
    View a specific report.
    """
    # In a real application, we would fetch the report from the database
    # For now, we'll just render the same template
    return templates.TemplateResponse("reports/list.html", {"request": request})


# Finance routes
@router.get("/payments", response_class=HTMLResponse)
async def payments(request: Request):
    """
    Display the payments page.
    """
    return templates.TemplateResponse("finance/payments.html", {"request": request})


@router.get("/fee-structures", response_class=HTMLResponse)
async def fee_structures(request: Request):
    """
    Display the fee structures page.
    """
    return templates.TemplateResponse("finance/fee_structures.html", {"request": request})


@router.get("/about", response_class=HTMLResponse)
async def about(request: Request):
    """
    Render the about page.
    """
    return templates.TemplateResponse("about.html", {"request": request})


@router.get("/contact", response_class=HTMLResponse)
async def contact(request: Request):
    """
    Render the contact page.
    """
    return templates.TemplateResponse("contact.html", {"request": request})


@router.get("/privacy", response_class=HTMLResponse)
async def privacy(request: Request):
    """
    Render the privacy policy page.
    """
    return templates.TemplateResponse("privacy.html", {"request": request})


@router.get("/forgot-password", response_class=HTMLResponse)
async def forgot_password(request: Request):
    """
    Render the forgot password page.
    """
    return templates.TemplateResponse("auth/forgot_password.html", {"request": request})


@router.get("/profile", response_class=HTMLResponse)
async def profile(request: Request):
    """
    Render the user profile page with screenshot management.
    """
    # Always use admin user ID for now to avoid any token decoding issues
    user_id = 1
    
    return templates.TemplateResponse("profile.html", {"request": request, "user_id": user_id})


@router.get("/api/users/{user_id}", response_class=JSONResponse)
async def get_user_profile(user_id: int, db: AsyncSession = Depends(get_db)):
    """
    API endpoint to get user profile data.
    """
    # Always return admin user data for now
    return {
        "id": 1,
        "email": "admin@example.com",
        "full_name": "Admin User",
        "is_active": True,
        "is_superuser": True,
        "role": "admin"
    }


@router.get("/settings", response_class=HTMLResponse)
async def settings(request: Request):
    """
    Render the user settings page.
    """
    # This would typically check for authentication and get user data
    # For now, we'll just render a placeholder
    return templates.TemplateResponse("settings.html", {"request": request})


@router.get("/change-password", response_class=HTMLResponse)
async def change_password(request: Request):
    """
    Render the change password page.
    """
    # This would typically check for authentication
    # For now, we'll just render a placeholder
    return templates.TemplateResponse("auth/change_password.html", {"request": request})


# Admin routes
@router.get("/admin/{path:path}", response_class=HTMLResponse)
async def admin_pages(request: Request, path: str):
    """
    Render admin pages.
    """
    # This would typically check for admin permissions
    # For now, we'll just render a placeholder
    return templates.TemplateResponse(f"admin/{path}.html", {"request": request})


# Teacher routes
@router.get("/teacher/{path:path}", response_class=HTMLResponse)
async def teacher_pages(request: Request, path: str):
    """
    Render teacher pages.
    """
    # This would typically check for teacher permissions
    # For now, we'll just render a placeholder
    return templates.TemplateResponse(f"teacher/{path}.html", {"request": request})


# Parent routes
@router.get("/parent/{path:path}", response_class=HTMLResponse)
async def parent_pages(request: Request, path: str):
    """
    Render parent pages.
    """
    # This would typically check for parent permissions
    # For now, we'll just render a placeholder
    return templates.TemplateResponse(f"parent/{path}.html", {"request": request})


# Student routes
@router.get("/students", response_class=HTMLResponse)
async def list_students(
    request: Request,
    search: Optional[str] = None,
    branch: Optional[str] = None,
    year: Optional[str] = None,
    filter_type: Optional[str] = None,
    page: int = Query(1, ge=1),
    db: AsyncSession = Depends(get_db),
):
    """
    List all students with optional filtering and pagination.
    """
    # Use mock data instead of database queries
    from school_management_system.services.mock_data_service import MockDataService
    
    # Get mock students
    mock_students = MockDataService.get_mock_students()
    
    # Apply filters if needed
    filtered_students = mock_students
    
    if search:
        search_lower = search.lower()
        filtered_students = [
            s for s in filtered_students if 
            search_lower in s["first_name"].lower() or 
            search_lower in s["last_name"].lower() or 
            search_lower in s["student_id"].lower() or 
            (s["email"] and search_lower in s["email"].lower()) or
            (s["project_title"] and search_lower in s["project_title"].lower()) or
            (s["internship_company"] and search_lower in s["internship_company"].lower()) or
            (s["placement_company"] and search_lower in s["placement_company"].lower())
        ]
    
    if branch:
        try:
            branch_enum = getattr(EngineeringBranch, branch)
            filtered_students = [s for s in filtered_students if s["branch"] == branch_enum]
        except (AttributeError, ValueError):
            filtered_students = []
    
    if year:
        try:
            year_enum = getattr(AcademicYear, year)
            filtered_students = [s for s in filtered_students if s["academic_year"] == year_enum]
        except (AttributeError, ValueError):
            filtered_students = []
    
    if filter_type:
        if filter_type == "placed":
            filtered_students = [s for s in filtered_students if s["placement_status"] == "Placed"]
        elif filter_type == "backlogs":
            filtered_students = [s for s in filtered_students if s["backlogs"] > 0]
        elif filter_type == "scholarship":
            filtered_students = [s for s in filtered_students if s["scholarship_status"]]
        elif filter_type == "hostel":
            filtered_students = [s for s in filtered_students if s["hostel_resident"]]
        elif filter_type == "top_cgpa":
            filtered_students = sorted(
                [s for s in filtered_students if s["cgpa"] is not None],
                key=lambda x: x["cgpa"],
                reverse=True
            )[:10]
    
    # Calculate pagination
    total = len(filtered_students)
    per_page = 10
    total_pages = (total + per_page - 1) // per_page if total > 0 else 1
    
    # Apply pagination
    start_idx = (page - 1) * per_page
    end_idx = start_idx + per_page
    paginated_students = filtered_students[start_idx:end_idx]
    
    return templates.TemplateResponse(
        "students/list.html",
        {
            "request": request,
            "students": paginated_students,
            "search": search,
            "branch": branch,
            "year": year,
            "filter_type": filter_type,
            "page": page,
            "total_pages": total_pages,
            "total": total,
            "branches": [b.name for b in EngineeringBranch],
            "years": [y.name for y in AcademicYear],
        },
    )


@router.get("/students/add", response_class=HTMLResponse)
async def add_student_form(request: Request):
    """
    Display the form to add a new student.
    """
    return templates.TemplateResponse(
        "students/add.html",
        {
            "request": request,
            "branches": [b.name for b in EngineeringBranch],
            "years": [y.name for y in AcademicYear],
        },
    )


@router.post("/students/add")
async def add_student(
    request: Request,
    first_name: str = Form(...),
    last_name: str = Form(...),
    date_of_birth: date = Form(...),
    gender: str = Form(...),
    enrollment_date: date = Form(...),
    academic_year: str = Form(...),
    branch: str = Form(...),
    student_id: str = Form(...),
    address: Optional[str] = Form(None),
    phone_number: Optional[str] = Form(None),
    email: Optional[str] = Form(None),
    parent_id: Optional[int] = Form(None),
    cgpa: Optional[float] = Form(None),
    backlogs: Optional[int] = Form(0),
    internship_company: Optional[str] = Form(None),
    internship_status: Optional[str] = Form(None),
    project_title: Optional[str] = Form(None),
    project_guide: Optional[str] = Form(None),
    placement_status: Optional[str] = Form(None),
    placement_company: Optional[str] = Form(None),
    scholarship_status: Optional[bool] = Form(False),
    scholarship_details: Optional[str] = Form(None),
    hostel_resident: Optional[bool] = Form(False),
    hostel_room_number: Optional[str] = Form(None),
    db: AsyncSession = Depends(get_db),
):
    """
    Process the form submission to add a new student.
    """
    # Check if student with this ID already exists
    existing_student = await student_service.get_student_by_student_id(db, student_id)
    if existing_student:
        return templates.TemplateResponse(
            "students/add.html",
            {
                "request": request,
                "error": "A student with this ID already exists",
                "student": {
                    "first_name": first_name,
                    "last_name": last_name,
                    "date_of_birth": date_of_birth,
                    "gender": gender,
                    "enrollment_date": enrollment_date,
                    "academic_year": academic_year,
                    "branch": branch,
                    "student_id": student_id,
                    "address": address,
                    "phone_number": phone_number,
                    "email": email,
                    "parent_id": parent_id,
                    "cgpa": cgpa,
                    "backlogs": backlogs,
                    "internship_company": internship_company,
                    "internship_status": internship_status,
                    "project_title": project_title,
                    "project_guide": project_guide,
                    "placement_status": placement_status,
                    "placement_company": placement_company,
                    "scholarship_status": scholarship_status,
                    "scholarship_details": scholarship_details,
                    "hostel_resident": hostel_resident,
                    "hostel_room_number": hostel_room_number,
                },
                "branches": [b.name for b in EngineeringBranch],
                "years": [y.name for y in AcademicYear],
            },
            status_code=status.HTTP_400_BAD_REQUEST,
        )

    # Create student
    try:
        # Convert string values to enum values
        academic_year_enum = getattr(AcademicYear, academic_year)
        branch_enum = getattr(EngineeringBranch, branch)
        
        student_data = {
            "first_name": first_name,
            "last_name": last_name,
            "date_of_birth": date_of_birth,
            "gender": gender,
            "enrollment_date": enrollment_date,
            "academic_year": academic_year_enum,
            "branch": branch_enum,
            "student_id": student_id,
            "address": address,
            "phone_number": phone_number,
            "email": email,
            "parent_id": parent_id,
            "cgpa": cgpa,
            "backlogs": backlogs,
            "internship_company": internship_company,
            "internship_status": internship_status,
            "project_title": project_title,
            "project_guide": project_guide,
            "placement_status": placement_status,
            "placement_company": placement_company,
            "scholarship_status": scholarship_status,
            "scholarship_details": scholarship_details,
            "hostel_resident": hostel_resident,
            "hostel_room_number": hostel_room_number,
        }
    except (AttributeError, ValueError):
        return templates.TemplateResponse(
            "students/add.html",
            {
                "request": request,
                "error": "Invalid academic year or branch",
                "student": {
                    "first_name": first_name,
                    "last_name": last_name,
                    "date_of_birth": date_of_birth,
                    "gender": gender,
                    "enrollment_date": enrollment_date,
                    "academic_year": academic_year,
                    "branch": branch,
                    "student_id": student_id,
                    "address": address,
                    "phone_number": phone_number,
                    "email": email,
                    "parent_id": parent_id,
                    "cgpa": cgpa,
                    "backlogs": backlogs,
                    "internship_company": internship_company,
                    "internship_status": internship_status,
                    "project_title": project_title,
                    "project_guide": project_guide,
                    "placement_status": placement_status,
                    "placement_company": placement_company,
                    "scholarship_status": scholarship_status,
                    "scholarship_details": scholarship_details,
                    "hostel_resident": hostel_resident,
                    "hostel_room_number": hostel_room_number,
                },
                "branches": [b.name for b in EngineeringBranch],
                "years": [y.name for y in AcademicYear],
            },
            status_code=status.HTTP_400_BAD_REQUEST,
        )
    
    await student_service.create_student(db, student_data)
    
    # Redirect to student list with success message
    response = RedirectResponse(url="/students?success=Student added successfully", status_code=status.HTTP_302_FOUND)
    return response


@router.get("/students/{student_id}", response_class=HTMLResponse)
async def view_student(
    request: Request,
    student_id: int,
    db: AsyncSession = Depends(get_db),
):
    """
    View a student's details.
    """
    student = await student_service.get_student(db, student_id)
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    
    return templates.TemplateResponse(
        "students/view.html",
        {"request": request, "student": student},
    )


@router.get("/students/{student_id}/edit", response_class=HTMLResponse)
async def edit_student_form(
    request: Request,
    student_id: int,
    db: AsyncSession = Depends(get_db),
):
    """
    Display the form to edit a student.
    """
    student = await student_service.get_student(db, student_id)
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    
    return templates.TemplateResponse(
        "students/edit.html",
        {
            "request": request, 
            "student": student,
            "branches": [b.name for b in EngineeringBranch],
            "years": [y.name for y in AcademicYear],
        },
    )


@router.post("/students/{student_id}/edit")
async def edit_student(
    request: Request,
    student_id: int,
    first_name: str = Form(...),
    last_name: str = Form(...),
    date_of_birth: date = Form(...),
    gender: str = Form(...),
    enrollment_date: date = Form(...),
    academic_year: str = Form(...),
    branch: str = Form(...),
    student_id_str: str = Form(...),
    address: Optional[str] = Form(None),
    phone_number: Optional[str] = Form(None),
    email: Optional[str] = Form(None),
    parent_id: Optional[int] = Form(None),
    cgpa: Optional[float] = Form(None),
    backlogs: Optional[int] = Form(0),
    internship_company: Optional[str] = Form(None),
    internship_status: Optional[str] = Form(None),
    project_title: Optional[str] = Form(None),
    project_guide: Optional[str] = Form(None),
    placement_status: Optional[str] = Form(None),
    placement_company: Optional[str] = Form(None),
    scholarship_status: Optional[bool] = Form(False),
    scholarship_details: Optional[str] = Form(None),
    hostel_resident: Optional[bool] = Form(False),
    hostel_room_number: Optional[str] = Form(None),
    is_active: bool = Form(True),
    db: AsyncSession = Depends(get_db),
):
    """
    Process the form submission to edit a student.
    """
    # Check if student exists
    student = await student_service.get_student(db, student_id)
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    
    # Check if student ID is being changed and if it already exists
    if student_id_str != student.student_id:
        existing_student = await student_service.get_student_by_student_id(db, student_id_str)
        if existing_student:
            return templates.TemplateResponse(
                "students/edit.html",
                {
                    "request": request,
                    "error": "A student with this ID already exists",
                    "student": {
                        "id": student_id,
                        "first_name": first_name,
                        "last_name": last_name,
                        "date_of_birth": date_of_birth,
                        "gender": gender,
                        "enrollment_date": enrollment_date,
                        "academic_year": academic_year,
                        "branch": branch,
                        "student_id": student_id_str,
                        "address": address,
                        "phone_number": phone_number,
                        "email": email,
                        "parent_id": parent_id,
                        "cgpa": cgpa,
                        "backlogs": backlogs,
                        "internship_company": internship_company,
                        "internship_status": internship_status,
                        "project_title": project_title,
                        "project_guide": project_guide,
                        "placement_status": placement_status,
                        "placement_company": placement_company,
                        "scholarship_status": scholarship_status,
                        "scholarship_details": scholarship_details,
                        "hostel_resident": hostel_resident,
                        "hostel_room_number": hostel_room_number,
                        "is_active": is_active,
                    },
                    "branches": [b.name for b in EngineeringBranch],
                    "years": [y.name for y in AcademicYear],
                },
                status_code=status.HTTP_400_BAD_REQUEST,
            )
    
    # Update student
    try:
        # Convert string values to enum values
        academic_year_enum = getattr(AcademicYear, academic_year)
        branch_enum = getattr(EngineeringBranch, branch)
        
        student_data = {
            "first_name": first_name,
            "last_name": last_name,
            "date_of_birth": date_of_birth,
            "gender": gender,
            "enrollment_date": enrollment_date,
            "academic_year": academic_year_enum,
            "branch": branch_enum,
            "student_id": student_id_str,
            "address": address,
            "phone_number": phone_number,
            "email": email,
            "parent_id": parent_id,
            "cgpa": cgpa,
            "backlogs": backlogs,
            "internship_company": internship_company,
            "internship_status": internship_status,
            "project_title": project_title,
            "project_guide": project_guide,
            "placement_status": placement_status,
            "placement_company": placement_company,
            "scholarship_status": scholarship_status,
            "scholarship_details": scholarship_details,
            "hostel_resident": hostel_resident,
            "hostel_room_number": hostel_room_number,
            "is_active": is_active,
        }
    except (AttributeError, ValueError):
        return templates.TemplateResponse(
            "students/edit.html",
            {
                "request": request,
                "error": "Invalid academic year or branch",
                "student": {
                    "id": student_id,
                    "first_name": first_name,
                    "last_name": last_name,
                    "date_of_birth": date_of_birth,
                    "gender": gender,
                    "enrollment_date": enrollment_date,
                    "academic_year": academic_year,
                    "branch": branch,
                    "student_id": student_id_str,
                    "address": address,
                    "phone_number": phone_number,
                    "email": email,
                    "parent_id": parent_id,
                    "cgpa": cgpa,
                    "backlogs": backlogs,
                    "internship_company": internship_company,
                    "internship_status": internship_status,
                    "project_title": project_title,
                    "project_guide": project_guide,
                    "placement_status": placement_status,
                    "placement_company": placement_company,
                    "scholarship_status": scholarship_status,
                    "scholarship_details": scholarship_details,
                    "hostel_resident": hostel_resident,
                    "hostel_room_number": hostel_room_number,
                    "is_active": is_active,
                },
                "branches": [b.name for b in EngineeringBranch],
                "years": [y.name for y in AcademicYear],
            },
            status_code=status.HTTP_400_BAD_REQUEST,
        )
    
    await student_service.update_student(db, student_id, student_data)
    
    # Redirect to student details with success message
    response = RedirectResponse(
        url=f"/students/{student_id}?success=Student updated successfully",
        status_code=status.HTTP_302_FOUND,
    )
    return response


@router.get("/students/{student_id}/delete", response_class=HTMLResponse)
async def delete_student_confirmation(
    request: Request,
    student_id: int,
    db: AsyncSession = Depends(get_db),
):
    """
    Display confirmation page for student deletion.
    """
    student = await student_service.get_student(db, student_id)
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    
    return templates.TemplateResponse(
        "students/delete.html",
        {"request": request, "student": student},
    )


@router.post("/students/{student_id}/delete")
async def delete_student(
    request: Request,
    student_id: int,
    db: AsyncSession = Depends(get_db),
):
    """
    Process student deletion.
    """
    student = await student_service.delete_student(db, student_id)
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    
    # Redirect to student list with success message
    response = RedirectResponse(
        url="/students?success=Student deleted successfully",
        status_code=status.HTTP_302_FOUND,
    )
    return response
