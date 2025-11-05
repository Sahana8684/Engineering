from typing import List, Optional, Dict, Any
from datetime import date
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy import update, delete, desc

from school_management_system.models.student import Student, EngineeringBranch, AcademicYear


async def get_student(db: AsyncSession, student_id: int) -> Optional[Student]:
    """
    Get a student by ID.
    """
    result = await db.execute(select(Student).where(Student.id == student_id))
    return result.scalars().first()


async def get_student_by_student_id(db: AsyncSession, student_id: str) -> Optional[Student]:
    """
    Get a student by their student ID (not the primary key).
    """
    result = await db.execute(select(Student).where(Student.student_id == student_id))
    return result.scalars().first()


async def get_students(
    db: AsyncSession, skip: int = 0, limit: int = 100
) -> List[Student]:
    """
    Get all students with pagination.
    """
    result = await db.execute(select(Student).offset(skip).limit(limit))
    return result.scalars().all()


async def create_student(db: AsyncSession, student_data: Dict[str, Any]) -> Student:
    """
    Create a new student.
    """
    student = Student(**student_data)
    db.add(student)
    await db.commit()
    await db.refresh(student)
    return student


async def update_student(
    db: AsyncSession, student_id: int, student_data: Dict[str, Any]
) -> Optional[Student]:
    """
    Update a student's information.
    """
    student = await get_student(db, student_id)
    if not student:
        return None

    for key, value in student_data.items():
        setattr(student, key, value)

    await db.commit()
    await db.refresh(student)
    return student


async def delete_student(db: AsyncSession, student_id: int) -> Optional[Student]:
    """
    Delete a student.
    """
    student = await get_student(db, student_id)
    if not student:
        return None

    await db.delete(student)
    await db.commit()
    return student


async def get_students_by_grade(db: AsyncSession, grade_level: str) -> List[Student]:
    """
    Get students by grade level.
    """
    result = await db.execute(select(Student).where(Student.grade_level == grade_level))
    return result.scalars().all()


async def get_students_by_parent(db: AsyncSession, parent_id: int) -> List[Student]:
    """
    Get students by parent ID.
    """
    result = await db.execute(select(Student).where(Student.parent_id == parent_id))
    return result.scalars().all()


async def search_students(
    db: AsyncSession, search_term: str, skip: int = 0, limit: int = 100
) -> List[Student]:
    """
    Search for students by name or student ID.
    """
    search_pattern = f"%{search_term}%"
    result = await db.execute(
        select(Student)
        .where(
            (Student.first_name.ilike(search_pattern))
            | (Student.last_name.ilike(search_pattern))
            | (Student.student_id.ilike(search_pattern))
            | (Student.email.ilike(search_pattern))
            | (Student.project_title.ilike(search_pattern))
            | (Student.internship_company.ilike(search_pattern))
            | (Student.placement_company.ilike(search_pattern))
        )
        .offset(skip)
        .limit(limit)
    )
    return result.scalars().all()


async def get_students_by_branch(
    db: AsyncSession, branch: EngineeringBranch, skip: int = 0, limit: int = 100
) -> List[Student]:
    """
    Get students by engineering branch.
    """
    result = await db.execute(
        select(Student).where(Student.branch == branch).offset(skip).limit(limit)
    )
    return result.scalars().all()


async def get_students_by_academic_year(
    db: AsyncSession, academic_year: AcademicYear, skip: int = 0, limit: int = 100
) -> List[Student]:
    """
    Get students by academic year.
    """
    result = await db.execute(
        select(Student).where(Student.academic_year == academic_year).offset(skip).limit(limit)
    )
    return result.scalars().all()


async def get_placed_students(
    db: AsyncSession, skip: int = 0, limit: int = 100
) -> List[Student]:
    """
    Get all placed students.
    """
    result = await db.execute(
        select(Student).where(Student.placement_status == "Placed").offset(skip).limit(limit)
    )
    return result.scalars().all()


async def get_students_with_backlogs(
    db: AsyncSession, skip: int = 0, limit: int = 100
) -> List[Student]:
    """
    Get students with backlogs.
    """
    result = await db.execute(
        select(Student).where(Student.backlogs > 0).offset(skip).limit(limit)
    )
    return result.scalars().all()


async def get_students_with_scholarship(
    db: AsyncSession, skip: int = 0, limit: int = 100
) -> List[Student]:
    """
    Get students with scholarships.
    """
    result = await db.execute(
        select(Student).where(Student.scholarship_status == True).offset(skip).limit(limit)
    )
    return result.scalars().all()


async def get_hostel_residents(
    db: AsyncSession, skip: int = 0, limit: int = 100
) -> List[Student]:
    """
    Get students who are hostel residents.
    """
    result = await db.execute(
        select(Student).where(Student.hostel_resident == True).offset(skip).limit(limit)
    )
    return result.scalars().all()


async def get_top_students_by_cgpa(
    db: AsyncSession, limit: int = 10
) -> List[Student]:
    """
    Get top students by CGPA.
    """
    result = await db.execute(
        select(Student).where(Student.cgpa.isnot(None)).order_by(desc(Student.cgpa)).limit(limit)
    )
    return result.scalars().all()


async def get_students_by_internship_status(
    db: AsyncSession, status: str, skip: int = 0, limit: int = 100
) -> List[Student]:
    """
    Get students by internship status.
    """
    result = await db.execute(
        select(Student).where(Student.internship_status == status).offset(skip).limit(limit)
    )
    return result.scalars().all()
