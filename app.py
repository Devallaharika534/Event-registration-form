from flask import Flask,render_template,request
app=Flask(_name_)
@app.route('\'.methods=['GET','POST'])
defindex():
  success_meassages=None
  if request.method=='POST':
      name=request.form.get('name')
      email=request.form.get('email')
      phone=request.form.get('phone')
      success_message=f"thank you for registering{name}!"
  return render_template("index.html",success_message)
  if__name__='__main__':
    app.run(host='0.0.0.0',port=5000)