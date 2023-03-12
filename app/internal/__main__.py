from datetime import datetime, timezone

import streamlit as st
from dash import Dash, dcc, html

st.set_page_config(page_title="Calendar App", layout="wide")

# Header for page
st.markdown(
    """
    <style>
        h2 {
            text-align: center;
        }
    </style>
    ## Calendar App
    ---
    """,
    unsafe_allow_html=True,
)

# Create 3 columns
# cols[0] will be 1/(1+2+1) = 25%
# cols[1] will be 2/(1+2+1) = 50%
# cols[2] will be 1/(1+2+1) = 25%
cols = st.columns([1, 2, 1])


def on_cal_date_change(*args, **kwargs):
    print(f"Calendar date changed: {args} {kwargs}")
    # This allows the JS to re-render and open the popover again...
    update_state = st.session_state.get("session_state_update", True)
    st.session_state["session_state_update"] = not update_state


local_dt = datetime.now(timezone.utc).astimezone().tzinfo
now = datetime.now(local_dt)
d = cols[1].date_input(
    label="When's your birthday",
    value=now.date(),
    on_change=on_cal_date_change,
)

# Try this out using dash
app = Dash(__name__)
app.layout = html.Div(
    [
        dcc.DatePickerSingle(
            id="my-date-picker-single",
            # initial_visible_month=now.date(),
            date=now.date(),
            stay_open_on_select=True,
        ),
        html.Div(id="output-container-date-picker-single"),
    ]
)

"""
st.components.v1.html(
    f""\"
        <div>some hidden container</div>
        <p>{st.session_state}</p>
        <script>
            // var input = window.parent.document.querySelectorAll("input[type=text]");
            var input = window.parent.document.querySelectorAll("input[type=text]");

            for (var i = 0; i < input.length; ++i) {{
                input[i].focus();
                input[i].width = "fit-content";
            }}
        </script>
    ""\",
    height=150,
)
"""

# st.write("Your birthday is:", d)
cols[1].markdown(
    f"""
    ##### Your birthday is: `{d}`
    """
)


if __name__ == "__main__":
    print("Hello World!")
    app.run_server(debug=True, use_reloader=False)
