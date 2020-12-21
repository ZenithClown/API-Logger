<div align="center">
  
  <table style="width:100%; border-collapse: collapse; border: none;">
    <tr>
      <th><a href = "https://zenithclown.github.io/minimalist-resume/"><img height = "128" width = "128" src = "./assets/logIcon.png"></a></th>
      <th>
        <h1 align = "center">REST API with Logging Functionalities</h1>
        <a href="https://github.com/ZenithClown/API-Logger/issues"><img alt="GitHub issues" src="https://img.shields.io/github/issues/ZenithClown/API-Logger?style=plastic"></a>
        <a href="https://github.com/ZenithClown/API-Logger/network"><img alt="GitHub forks" src="https://img.shields.io/github/forks/ZenithClown/API-Logger?style=plastic"></a>
        <a href="https://github.com/ZenithClown/API-Logger/stargazers"><img alt="GitHub stars" src="https://img.shields.io/github/stars/ZenithClown/API-Logger?style=plastic"></a>
        <a href="https://github.com/ZenithClown/API-Logger"><img alt="GitHub license" src="https://img.shields.io/github/license/ZenithClown/API-Logger?style=plastic"></a>
      </th>
    </tr>
  </table>

</div>

<p align="justify">A simple <b>REST API</b> design, built using <code>flask_restful</code>, implemented with advanced <code>logging</code> functionalities. For demonstration purpose, there is one <code>controller</code> which raises a <code>ZeroDivisionError</code> for the API accesible at <code>localhost:5000/home</code>.</p>

## Setup

<p align="justify">A list of <i>tentative</i> packages is available in <code>requirements.txt</code>. This module can be run using <code>python 3.6+</code> since it uses the <i>f-string</i> functionality. However, it is better to run in <code>python 3.7+</code> as <code>importlib.resources</code> has been used to initialize logger configuration from <code>app/static/logger.yaml</code> file.</p>

```python
pip install -r requirements.txt # install all requirements from command line
```

### YAML Configuration File

Flask by default uses the `logging` module for logging and debugging into console - which can be _custom_ built using the following:

- [Dictionary Schema](https://docs.python.org/3/library/logging.config.html#configuration-dictionary-schema), and
- [Calling `logging` Class](https://www.youtube.com/watch?v=jxmzY9soFXg&t=945s).

<p align="justify">In this template/project, a YAML file is used, as given in documentation, to configure different types of loggers - namely <code>DEBUG</code>, <code>ERROR</code> and others - which is defined in <code>app/__init__.py</code> so that it is available for the total package. General convention to log a message:</p>

```bash
loggerName.loggerLevel("<log message>")
```
