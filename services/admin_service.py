from database.db_connection import run_query
from models.models import Admin
from typing import Optional, List, Dict, Any

class AdminService:
    """Service class for admin-related operations"""
    
    @staticmethod
    def authenticate(username: str, password: str) -> bool:
        """
        Authenticate an admin user.
        
        Args:
            username: Admin username
            password: Admin password
            
        Returns:
            bool: True if authentication successful, False otherwise
        """
        # Use parameterized query for security
        cred = run_query("SELECT * FROM admin WHERE username = %s AND password = %s;", (username, password))
        return bool(cred)
    
    @staticmethod
    def get_admin(username: str) -> Optional[Admin]:
        """
        Get admin by username.
        
        Args:
            username: Admin username
            
        Returns:
            Optional[Admin]: Admin object if found, None otherwise
        """
        result = run_query("SELECT username, password FROM admin WHERE username = %s;", (username,))
        if result and len(result) > 0:
            admin_data = result[0]
            return Admin(username=admin_data[0], password=admin_data[1])
        return None