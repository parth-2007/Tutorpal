<template>
  <form>
    <div style="margin-top: 15px" class="mb-3">
      <label for="emailaddress" class="form-label">Email Address</label>
      <input type="email" class="form-control" id="emailaddress" required />
    </div>
    <div class="mb-3">
      <label for="firstname" class="form-label">First Name</label>
      <input class="form-control" id="firstname" required />
    </div>
    <div class="mb-3">
      <label for="lastname" class="form-label">Last Name</label>
      <input class="form-control" id="lastname" required />
    </div>
    <div class="mb-3">
      <label for="occupation" class="form-label">Occupation</label>
      <input class="form-control" id="occupation" required />
    </div>
    <div class="mb-3">
      <label for="subject" class="form-label">Subjects</label>
      <input class="form-control" id="subject" required />
    </div>
    <div class="text-block-5"><b>Class Description</b></div>
    <textarea
      style="height: 250px"
      class="form-control"
      id="description"
      rows="3"
    ></textarea>
    <div style="margin-top: 15px" class="row">
      <div class="col">
        <label for="major" class="form-label">Major</label>
        <input type="text" class="form-control" id="major" required />
      </div>
      <div style="padding-left: 0px" class="col">
        <label for="gpa" class="form-label">GPA</label>
        <input type="number" id="gpa" min="0" max="5" class="form-control" />
      </div>
      <div style="padding-left: 0px" class="col">
        <label for="education" class="form-label">Education</label>
        <select
          style="margin-top: 0px"
          class="form-select"
          id="education"
          aria-label="Default select example"
        >
          <option selected>Select</option>
          <option value="1">Highschooler</option>
          <option value="2">College Student</option>
          <option value="3">Bachelors</option>
          <option value="4">Masters</option>
          <option value="4">PhD</option>
        </select>
      </div>
      <div style="padding-left: 0px" class="col">
        <label for="school" class="form-label">School/College</label>
        <input type="text" class="form-control" id="school" required />
      </div>
    </div>
    <textarea
      style="height: 250px; margin-top: 25px"
      class="form-control"
      placeholder="Qualifications"
      id="educationdescription"
      rows="3"
    ></textarea>
    <div style="margin-top: 15px; margin-bottom: 5px" class="text-block-5">
      <b>Linkedin Profile Link(Optional)</b>
    </div>
    <input
      class="form-control"
      id="linkedin"
      placeholder="https://www.linkedin.com/in/johndoe"
    />
    <div class="row">
      <div class="col">
        <textarea
          style="height: 250px; margin-top: 25px"
          class="form-control"
          id="bio"
          placeholder="Eg. My hobbies are..."
          rows="3"
        ></textarea>
      </div>
      <div style="padding-left: 0px" class="col">
        <div style="position: relative; text-align: center" class="col">
          <p>
            <input
              type="file"
              accept="image/"
              name="image"
              id="file"
              onchange="loadFile(event)"
              style="display: none"
            />
          </p>
          <label for="file" style="cursor: pointer"
            ><p>
              <img
                style="border-radius: 400px"
                src="../static/tutor/images/user-2.png"
                id="output"
                width="250"
                height="250"
              /></p
          ></label>
          <label
            style="
              position: absolute;
              top: 50%;
              left: 50%;
              transform: translate(-50%, -50%);
            "
            class="form-label"
            >Upload</label
          >
        </div>
      </div>
    </div>
    <label
      style="margin-top: 15px"
      for="rates"
      id="pricedisplay"
      class="form-label"
      >Pricing: $500</label
    >
    <input type="range" min="0" max="1000" class="form-range" id="rates" />
    <div style="margin-top: 15px" class="row">
      <div class="col">
        <label for="teachexp" class="form-label"
          >Years of Teaching Experience</label
        >
        <input
          type="number"
          id="teachexp"
          min="0"
          max="30"
          class="form-control"
        />
      </div>
      <div style="padding-left: 0px" class="col">
        <label for="profexp" class="form-label"
          >Years of Professional Experience</label
        >
        <input
          id="profexp"
          type="number"
          min="0"
          max="30"
          class="form-control"
        />
      </div>
    </div>
    <label style="margin-top: 15px" for="availability" class="form-label"
      >Availability</label
    >
    <input
      class="form-control"
      id="availability"
      placeholder="Mondays, 4:00 PM - 6:00 PM"
    />
    <label style="margin-top: 15px" for="password" class="form-label"
      >Verify Password</label
    >
    <input type="password" class="form-control" id="password" required />
    <button
      style="margin-top: 15px; font-family: Poppins; margin-left: 0px"
      class="btn btn-primary"
    >
      Update Profile
    </button>
  </form>
</template>

<script>
export default {
  data() {
    return {
      email: '',
      firstName: '',
      lastName: '',
      profilePic: null,
      paypalEmail: '', // missing
      birthDate: '', // missing
      gender: '', // missing
      occupation: '',
      subjects: '',
      whatYouTeach: '',
      major: '',
      gpa: 0,
      education: '',
      school: '',
      qualifications: '',
      linkedIn: '',
      bio: '',
      rates: 0,
      teachExp: 0,
      profExp: 0,
      availability: '',
      errors: {
        toc: '',
        email: '',
        firstName: '',
        lastName: '',
        password: '',
        confirmPassword: '',
        profilePic: '',
        paypalEmail: '',
        birthDate: '',
        gender: '',
        occupation: '',
        subjects: '',
        whatYouTeach: '',
        major: '',
        gpa: '',
        education: '',
        school: '',
        qualifications: '',
        linkedIn: '',
        bio: '',
        rates: '',
        teachExp: '',
        profExp: '',
        availability: '',
        global: '',
      },
    }
  },
}
</script>