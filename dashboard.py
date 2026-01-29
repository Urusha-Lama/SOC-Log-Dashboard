import streamlit as st
from parse_windows import parse_windows_logs
from parse_firewall import parse_firewall_logs
from detection_engine import detect_windows, detect_firewall

st.set_page_config(page_title="Mini SIEM Dashboard", layout="wide")
st.title("🛡️ Mini SIEM Dashboard")

log_type = st.selectbox(
    "Select Log Source",
    ["Windows Logs", "Firewall Logs"]
)

if log_type == "Windows Logs":
    st.subheader("Windows Security Logs")

    events = parse_windows_logs("windows_logs.txt")
    alerts = detect_windows(events)

    st.write("### Parsed Logs")
    st.table(events)

    st.write("### Alerts")
    if alerts:
        for a in alerts:
            st.error(a)
    else:
        st.success("No threats detected")

else:
    st.subheader("Firewall Logs")

    events = parse_firewall_logs("firewall_logs.txt")
    alerts = detect_firewall(events)

    st.write("### Parsed Logs")
    st.table(events)

    st.write("### Alerts")
    if alerts:
        for a in alerts:
            st.error(a)
    else:
        st.success("No threats detected")
