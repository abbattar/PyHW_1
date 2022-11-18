from view import user_view

def create(user, user_id):
    style = 'style = "font-size:22px;"'
    html = '<html>\n <head></head>\n <body>\n'
    html += f'   <p {style}>User: {user_view(user, user_id)}</p>\n'
    html += '   </body>\n</html>'

    with open('index.html', 'w') as page:
        page.write(html)

    return html