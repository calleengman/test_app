import streamlit as st
# To make things easier later, we're also importing numpy and pandas for
# working with sample data.
import numpy as np
import pandas as pd

st.title('My first app')

st.write('Create a table:')
st.write(pd.DataFrame({
    'a':[1,2,3,4],
    'b':[10,20,30,40]
}))

"""
You can also write to your app without calling any Streamlit methods. Streamlit supports “magic commands,” which means you don’t have to use st.write() at all! 
"""

"""
# My first app
Here's our first attempt at using data to create a table:
"""

df = pd.DataFrame({
  'first column': [100, 200, 300, 400],
  'second column': [10, 20, 30, 40]
})

df

"""
Any time that Streamlit sees a variable or a literal value on its own line, it automatically writes that to your app using st.write(). For more information, refer to the documentation on magic commands.
"""



"""
## Draw a line chart
You can easily add a line chart to your app with st.line_chart(). We’ll generate a random sample using Numpy and then chart it.
"""

chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])

st.line_chart(chart_data)


"""
# Plot a map
With st.map() you can display data points on a map. Let’s use Numpy to generate some sample data and plot it on a map of San Francisco.
"""

map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])

st.map(map_data)

"""
# Add interactivity with widgets
With widgets, Streamlit allows you to bake interactivity directly into your apps with checkboxes, buttons, sliders, and more. Check out our API reference for a full list of interactive widgets.
"""
"""
## Use checkboxes to show/hide data
One use case for checkboxes is to hide or show a specific chart or section in an app. st.checkbox() takes a single argument, which is the widget label. In this sample, the checkbox is used to toggle a conditional statement.
"""

if st.checkbox('Show dataframe'):
    chart_data = pd.DataFrame(
       np.random.randn(20, 3),
       columns=['a', 'b', 'c'])

    st.line_chart(chart_data)

"""
## Use a selectbox for options
Use st.selectbox to choose from a series. You can write in the options you want, or pass through an array or data frame column.

Let’s use the df data frame we created earlier.
"""
option1 = st.selectbox(
    'Which number do you like best?',
     df['first column'])

'You selected: ', option1

"""
## Lay out your app
For a cleaner look, you can move your widgets into a sidebar. This keeps your app central, while widgets are pinned to the left. Let’s take a look at how you can use st.sidebar in your app.
"""
option2 = st.sidebar.selectbox(
    'Which other number do you like best?',
     df['first column'])

'You selected:', option2

"""
Most of the elements you can put into your app can also be put into a sidebar using this syntax: st.sidebar.[element_name](). Here are a few examples that show how it’s used: st.sidebar.markdown(), st.sidebar.slider(), st.sidebar.line_chart().

You can also use st.beta_columns to lay out widgets side-by-side, or st.beta_expander to conserve space by hiding away large content.
"""
left_column, right_column = st.beta_columns(2)
pressed = left_column.button('Press me?')
if pressed:
    right_column.write("Woohoo!")

expander = st.beta_expander("FAQ")
expander.write("Here you could put in some really, really long explanations...")


"""
# Show progress
When adding long running computations to an app, you can use st.progress() to display status in real time.

First, let’s import time. We’re going to use the time.sleep() method to simulate a long running computation:
"""
import time
"""
Now, let’s create a progress bar:
"""
'Starting a long computation...'

# Add a placeholder
latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
  # Update the progress bar with each iteration.
  latest_iteration.text(f'Iteration {i+1}')
  bar.progress(i + 1)
  time.sleep(0.1)

'...and now we\'re done!'