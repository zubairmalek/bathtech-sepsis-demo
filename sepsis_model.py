def check_sepsis_risk(heart_rate, temperature, respiratory_rate):
    if not (0 < heart_rate < 300):
        raise ValueError("Heart rate outside clinical range")
    if not (30 < temperature < 45):
        raise ValueError("Temperature outside clinical range")
    if not (0 < respiratory_rate < 60):
        raise ValueError("Respiratory rate outside clinical range")
    
    score = 0
    if heart_rate > 90:
        score += 1
    if temperature > 38.3 or temperature < 36:
        score += 1
    if respiratory_rate > 20:
        score += 1
    
    return score >= 2
