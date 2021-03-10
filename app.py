import json
import plotly as py
import plotly.graph_objs as go

# replace 'example_data.json' with 'StreamingHistory.json', merge all StreamingHistory files if you received multiple
with open('example_data.json', 'r') as json_data:
  data = json.load(json_data)


def to_json(data):
  return json.dumps(data, indent=2)


def get_number_played():
  dictionary = {}

  for track in data:
    name = "{} – {}".format(track['trackName'], track['artistName'])

    if name in dictionary:
      dictionary[name] += 1
    else:
      dictionary[name] = 1

  sorted_dictionary = dict(sorted(dictionary.items(), key=lambda item: item[1], reverse=True))

  return sorted_dictionary


def get_tracks_hours_played():
  dictionary = {}

  for track in data:
    name = "{} - {}".format(track['trackName'], track['artistName'])

    if name in dictionary:
      dictionary[name] += track['msPlayed']
    else:
      dictionary[name] = track['msPlayed']

  sorted_dictionary = dict(sorted(dictionary.items(), key=lambda item: item[1], reverse=True))

  for key, value in sorted_dictionary.items():
    sorted_dictionary[key] = round(value / 1000 / 60 / 60, 2)

  return sorted_dictionary


def get_artist_hours_played():
  dictionary = {}

  for track in data:
    name = track['artistName']

    if name in dictionary:
      dictionary[name] += track['msPlayed']
    else:
      dictionary[name] = track['msPlayed']

  sorted_dictionary = dict(sorted(dictionary.items(), key=lambda item: item[1], reverse=True))

  for key, value in sorted_dictionary.items():
    sorted_dictionary[key] = round(value / 1000 / 60 / 60, 2)

  return sorted_dictionary


def draw_graph(data, title='title', x_title='x',
               y_title='y', font='Arial',
               font_color='#663399', bar_color='lightslategray',
               begin=0, end=10):
  artists = []
  time = []

  for key, value in data.items():
    artists.append(key)
    time.append(value)

  fig = go.Figure(data=[go.Bar(x=artists[begin:end], y=time[begin:end], marker_color=[bar_color] * end)])
  fig.update_layout(
      title=title,
      xaxis_title=x_title,
      yaxis_title=y_title,
      font=dict(
          family=font,
          size=18,
          color=font_color)
  )
  fig.show()


draw_graph(get_artist_hours_played(), title='artists listened to', y_title='hours', x_title='artists', begin=0, end=10)
draw_graph(get_tracks_hours_played(), title='tracks listened to', y_title='hours', x_title='tracks', begin=0, end=10)
draw_graph(get_number_played(), title='tracks listened to', y_title='number of times', x_title='tracks', begin=0, end=10)
