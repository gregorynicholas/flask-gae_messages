# flask-gae_messages

--------------

Flask extension for working with messages using the mail & xmpp apis on App Engine.

----

### install with pip
`pip install https://github.com/gregorynicholas/flask-gae_messages/tarball/master`

### usage

    from jinja2 import Environment
    from jinja2 import Template
    from jinja2.loaders import DictLoader
    env = Environment(loader=DictLoader({
      'subject.tpl': '{{var}}',
      'message.html.tpl': '<html>{{var}}</html>',
      'message.text.tpl': '{{var}}',
    }))

    message = gae_messages.Message(
      sender='test@domain.com',
      subject=env.get_template("subject.tpl"),
      template_html=env.get_template("message.html.tpl"),
      template_text=env.get_template("message.text.tpl"))

    message.send(
      to='test@gmail.com',
      replacements={'var': 'testing'},
      method=Method.EMAIL)
