import enum

add_roles = ['system_admin', 'school_admin', 'teacher', 'student', 'parent']


class BasicRoles(enum.Enum):
    STUDENT = "student"
    SYSTEM_ADMIN = "system_admin"
    SCHOOL_ADMIN = "school_admin"
    TEACHER = "teacher"
    PARENT = "parent"



