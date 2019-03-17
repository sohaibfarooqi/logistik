from flask import jsonify

def page_not_found(error):
  """
  Generic 404 Error handler
  """
  return jsonify({"code": 404, "message": "requested URL not found on server"}), 404

def intenal_server_error(error):
  """
  Generic 404 Error handler
  """
  print(error)
  return jsonify({"code": 500, "message": "requested URL not found on server"}), 500

