# main_model.py

from System.Common.base_model import BaseModel

class mainModel(BaseModel):

    def get_posts(self, post_ids):
        """Retrieve posts by ID"""
        ids = ", ".join(["?"] * len(post_ids))
        query = f"""
            SELECT * FROM [posts] WHERE id IN ({ids});
        """
        return self._select_query(query, *post_ids)

    def delete_posts(self, date_start, date_end):
        """Delete posts between start and end dates"""
        delete_query_states = """
            DELETE FROM [posts] 
            WHERE created >= ? AND created <= ?;
        """
        success, rowcount = self._execute_query(delete_query_states, date_start, date_end)
        if success:
            return {"message": "Records deleted successfully.", "deleted": rowcount}
        else:
            return {"error": "An error occurred during deletion."}