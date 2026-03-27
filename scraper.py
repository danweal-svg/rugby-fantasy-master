import pandas as pd

def sync_entire_league():
    # 1. MATCHUP DIFFICULTY MAP (Lower = Easier Opponent = Higher Fantasy Potential)
    # Based on 2026 defensive stats: Moana and Force are 'Tier 1' targets for points.
    difficulty_map = {
        "Moana Pasifika": 1, "Western Force": 1, "NSW Waratahs": 2, 
        "Fijian Drua": 2, "Highlanders": 3, "Crusaders": 3, 
        "Queensland Reds": 4, "Blues": 4, "Chiefs": 5, "ACT Brumbies": 5, "Hurricanes": 5
    }

    # 2. ROUND 7 FIXTURES (Who is playing who)
    fixtures = {
        "Brumbies": "NSW Waratahs", "Chiefs": "Western Force",
        "Hurricanes": "Queensland Reds", "Blues": "Fijian Drua",
        "Highlanders": "Moana Pasifika", "Crusaders": "BYE"
    }

    # 3. COMPREHENSIVE PLAYER DATA (James Slipper Included)
    league_data = [
        {"Player": "James Slipper", "Team": "Brumbies", "Pos": "Prop", "Season_Avg": 18.2, "Form": 20.1, "Status": "Starting"},
        {"Player": "Charlie Cale", "Team": "Brumbies", "Pos": "Back Row", "Season_Avg": 31.5, "Form": 38.2, "Status": "Starting"},
        {"Player": "Damian McKenzie", "Team": "Chiefs", "Pos": "Fly Half", "Season_Avg": 28.2, "Form": 30.5, "Status": "Starting"},
        {"Player": "Will Jordan", "Team": "Crusaders", "Pos": "Fullback", "Season_Avg": 29.0, "Form": 0.0, "Status": "BYE"},
        {"Player": "Billy Proctor", "Team": "Hurricanes", "Pos": "Center", "Season_Avg": 21.4, "Form": 26.3, "Status": "Starting"},
        {"Player": "Samisoni Taukei'aho", "Team": "Chiefs", "Pos": "Hooker", "Season_Avg": 23.8, "Form": 22.1, "Status": "Starting"},
        {"Player": "Jacob Ratumaitavuki-Kneepkens", "Team": "Highlanders", "Pos": "Fullback", "Season_Avg": 24.8, "Form": 26.5, "Status": "Starting"}
    ]
    
    df = pd.DataFrame(league_data)

    # 4. CALC THE MATCHUP BONUS
    def get_bonus(row):
        opp = fixtures.get(row['Team'], "None")
        if opp == "BYE" or opp == "None": return 0
        diff = difficulty_map.get(opp, 3)
        # Bonus: +10 pts for playing Tier 1 (Weak Defense), +5 for Tier 2
        if diff == 1: return 10
        if diff == 2: return 5
        return 0

    df['Matchup_Bonus'] = df.apply(get_bonus, axis=1)
    df['Priority_Score'] = df['Form'] + df['Matchup_Bonus']
    
    df.sort_values(by='Priority_Score', ascending=False).to_csv("season_stats.csv", index=False)
    print("✅ Matchup Intelligence Synced.")

if __name__ == "__main__":
    sync_entire_league()