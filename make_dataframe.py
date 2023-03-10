import pandas as pd
df = pd.DataFrame(columns=
             ['team1','team2','date','time','city','stadium','referee',
              'attendance','possesion_team1','possesion_team2','stage',
              'penalty_series_goals_team1', 'penalty_series_goals_team2',
              'goal_total_team1','goal_total_team2',
              'goal_conceded_team1',  'goal_conceded_team2',
              'goal_inside_penalty_area_team1', 'goal_inside_penalty_area_team2',
              'goal_outside_penalty_area_team1', 'goal_outside_penalty_area_team2',
              'goal_assists_team1','goal_assists_team2','attempts_total_team1',
             'attempts_total_team2','attempts_on_target_team1',
             'attempts_on_target_team2','attempts_off_target_team1',
             'attempts_off_target_team2','attempts_inside_penalty_area_team1',
             'attempts_inside_penalty_area_team2','attempts_outside_penalty_area_team1',
             'attempts_outside_penalty_area_team2',
             'final_third_entries_left_channel_team1',
             'final_third_entries_left_channel_team2',
             'final_third_entries_left_inside_channel_team1',
             'final_third_entries_left_inside_channel_team2',
             'final_third_entries_central_channel_team1',
             'final_third_entries_central_channel_team2',
             'final_third_entries_right_inside_channel_team1',
             'final_third_entries_right_inside_channel_team2',
             'final_third_entries_right_channel_team1', 
             'final_third_entries_right_channel_team2',
             'offers_total_team1','offers_total_team2','offers_in_behind_team1',
             'offers_in_behind_team2','offers_in_between_team1',
             'offers_in_between_team2','offers_in_front_team1',
             'offers_in_front_team2',
             'receptions_between_midfield_and_defensive_lines_team1',
             'receptions_between_midfield_and_defensive_lines_team2',
             'receptions_behind_defensive_line_team1',
             'receptions_behind_defensive_line_team2',
             'line_breaks_attempted_team1',
             'line_breaks_attempted_team2','line_breaks_completed_team1',
             'line_breaks_completed_team2','line_breaks_attempted_defensive_team1',
             'line_breaks_attempted_defensive_team2','line_breaks_completed_defensive_team1',
             'line_breaks_completed_defensive_team2','yellow_cards_team1',
             'yellow_card_team2','red_cards_team1','red_cards_team2','fouls_team1',
             'fouls_team2','offsides_team1','offsides_team2','passes_team1',
             'passes_team2','passes_completed_team1','passes_completed_team2',
             'crosses_team1','crosses_team2','crosses_completed_team1',
             'crosses_completed_team2','switches_of_play_completed_team1',
             'switches_of_play_completed_team2','corners_team1','corners_team2',
             'free_kicks_team1','free_kicks_team2','penalties_scored_team1',
             'penalties_scored_team2','goal_preventions_team1','goal_preventions_team2',
             'own_goals_team1','own_goals_team2','forced_turnovers_team1',
             'forced_turnovers_team2','defensive_pressures_applied_team1',
             'defensive_pressures_applied_team2'],index = range(64))
df.to_csv('empty_df.csv')