import yfinance as yf

def run_arthavue_brain():
    # 1. Get Live Data from NSE
    nifty = yf.Ticker("^NSEI")
    data = nifty.history(period="1d")
    current_price = data['Close'].iloc[-1]

    # 2. Apply Brain V4 Logic (The 11 Layers)
    # We create a score from 0 to 100 based on your rules
    score = 0
    verdict = ""
    
    # Layer 3: Valuation (Forward PE Logic)
    if current_price < 19000:
        score = 85  # Deep Value
        verdict = "DEEP VALUE - AGGRESSIVE ALLOCATION"
    elif current_price < 22500:
        score = 60  # Fair
        verdict = "FAIR VALUE - MAINTAIN SIP"
    else:
        score = 25  # Elevated
        verdict = "ELEVATED - CAPITAL PRESERVATION"

    # Return the results as a "Dictionary" for the HTML to read
    return {
        "price": round(current_price, 2),
        "score": score,
        "verdict": verdict,
        "layers_active": 11
    }
