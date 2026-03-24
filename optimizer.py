def optimize_path(mapped_data):
    # Minimal logic: prioritize max transferable credits, then min cost
    # For now, we return the mapped_data directly (can add sorting for multiple options later)
    return {
        "degree": mapped_data["degree"],
        "transferable_credits": mapped_data["transferable_credits"],
        "total_cost": mapped_data["total_cost"],
        "total_duration_weeks": mapped_data["total_duration_weeks"],
        "courses_needed": mapped_data["courses_needed"]
    }
