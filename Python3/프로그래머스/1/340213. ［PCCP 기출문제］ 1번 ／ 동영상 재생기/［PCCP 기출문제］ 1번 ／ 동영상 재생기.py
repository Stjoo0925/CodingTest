def time_to_seconds(time_str):
    mm, ss = map(int, time_str.split(":"))
    return mm * 60 + ss

def seconds_to_time(seconds):
    mm = seconds // 60
    ss = seconds % 60
    return f"{mm:02}:{ss:02}"

def solution(video_len, pos, op_start, op_end, commands):
    video_length = time_to_seconds(video_len)
    current_pos = time_to_seconds(pos)
    op_start_time = time_to_seconds(op_start)
    op_end_time = time_to_seconds(op_end)
    
    for command in commands:
        if op_start_time <= current_pos <= op_end_time:
            current_pos = op_end_time
        
        if command == "prev":
            current_pos = max(0, current_pos - 10)
        elif command == "next":
            current_pos = min(video_length, current_pos + 10)
    
    if op_start_time <= current_pos <= op_end_time:
        current_pos = op_end_time
    
    return seconds_to_time(current_pos)