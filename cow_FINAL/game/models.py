from django.db import models
# Create your models here.


'''

      <table border="3">
        {% for i in data.length_y %}
          <tr height=154>
          {% for j in data.length_x %}
            <th width=320>
            <table>
             {% if forloop.counter == data.Position_x1 %}
              {% if forloop.parentloop.counter == data.Position_y1 %}

                {% if data.Position_x1 == data.Position_x2 %}
                  {% if data.Position_y1 == data.Position_y2 %}
                    <th width=150>
                  {% else %}
                    <th width=320>
                  {% endif %}
                {% else %}
                  <th width=320>
                {% endif %}

              <img src="{% static data.character1 %}" width=105% height=150%>
                </th>

              {% endif %}
            {% endif %} 

            {% if forloop.counter == data.Position_x2 %}
              {% if forloop.parentloop.counter == data.Position_y2 %}
          
                {% if data.Position_x2 == data.Position_x1 %}
                  {% if data.Position_y2 == data.Position_y1 %}
                    <th width=150>
                  {% else %}
                    <th width=320>
                  {% endif %}
                {% else %}
                  <th width=320>
                {% endif %}
              <img src="{% static data.character2 %}" width=105% height=150%>
                </th>
              {% endif %}
            {% endif %}  
            </table>
            </th>
          {% endfor %}
          </tr>
        {% endfor %}
      </table>

'''