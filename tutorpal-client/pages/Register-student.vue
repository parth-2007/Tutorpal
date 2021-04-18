<template>
<client-only>
<html data-wf-page="5f59b13f87c4474926e0f928" data-wf-site="5f5844923df4f032aa587322">
<head>
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" crossorigin="anonymous">
</head>
<body style="height: 130vh;" class="body">
  <div style="height: 170vh;" class="section">
    <div style="font-family: Poppins; height: 750px; width: 500px;" class="div-block">
      <div style="margin-top: 40px;" class="div-block-4">
        <h1 class="heading">Create a student account</h1>
      </div>
      <div class="div-block-2">
        <div class="text-block">Already have an account?</div><a href="/login" class="link">Sign In</a></div>
      <div class="div-block-3">
        <div>
          <form method="post" enctype="multipart/form-data">
            <div class="row">
              <div class="col">
                <label for="firstname" class="form-label">First Name</label>
                <input type="text" class="form-control" id="firstname" aria-label="First name" required>
              </div>
              <div style="padding-left: 0px;" class="col">
                <label for="lastname" class="form-label">Last Name</label>
                <input type="text" class="form-control" id="lastname" aria-label="Last name" required>
              </div>
            </div>
            <div style="margin-top: 15px;" class="mb-3">
              <label for="emailaddress" class="form-label">Email Address</label>
              <input type="email" class="form-control" id="emailaddress" required>
            </div>
            <div class="row">
              <div class="col">
                <label for="password" class="form-label">Password</label>
                <input type="password" class="form-control" id="password" required>
              </div>
              <div style="padding-left: 0px;" class="col">
                <label for="confirmpassword" class="form-label">Confirm Password</label>
                <input type="password" class="form-control" id="confirmpassword" required>
              </div>
            </div>
            <div style="margin-top:15px; float: left;" class="row">
              <div style="position: relative; text-align: center;" class="col">
                <p><input type="file" accept="image/*" name="image" id="file" onchange="loadFile(event)" style="display: none;"></p>
                <label for="file" style="cursor: pointer;"><p><img style="border-radius:400px" src="../components/register/images/user-2.png" id="output" width="100" height="100"/></p></label>
                <label style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%);" class="form-label">Upload</label>
              </div>
            </div>
            <div style="margin-top: 25px;" class="mb-3">
              <input type="email" class="form-control" id="parentemail" placeholder="Enter Parent Email" required>
            </div>
            <div class="form-group row">
              <label for="birthdate" class="col-2 col-form-label">Birthdate</label>
              <div class="col-10">
                <input class="form-control" type="date" id="birthdate" required>
              </div>
            </div>
            <div style="margin-top: 15px; margin-bottom: 15px;" class="form-check">
              <input class="form-check-input" nam="checkbox" type="checkbox" id="toc" required>
              <label class="form-check-label" for="toc">
                I agree with the <a href="toc.html">Terms of Service</a>
              </label>
            </div>
            <button style="margin-bottom: 20px;" type="submit" class="btn btn-primary">Register</button>
          </form>
        </div>
      </div>
    </div>
  </div>
</body>
</html>
</client-only>
</template>
<style>

</style>
<script>
export default{
  head (){
    return{
      title: "Student Registration",
    }
  },
}

require('../components/register/css/webflow.css');
require('../components/register/css/2tor4u-2-0.webflow.css');
require('../components/register/css/normalize.css');

</script>
