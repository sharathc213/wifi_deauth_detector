function starti(image) {
  let csf = $("input[name=csrfmiddlewaretoken]").val();
  Swal.fire({
    title: 'Enter a Name for This Container',
    input: 'text',
    inputAttributes: {
      autocapitalize: 'off'
    },
    showCancelButton: true,
    confirmButtonText: 'Start',
    showLoaderOnConfirm: true,
    preConfirm: (name) => {
      
      var data = {
        image: image,
        name:name,
      };
      $.ajax({
        headers: { "X-CSRFToken": csf },
        mode: "same-origin", // Do not send CSRF token to another domain.
        beforeSend: function () {
          $(".preloader").css("visibility", "visible");
        },
        url: "/starti",
        type: "POST",
        data: data,
        dataType: "json",
        success: function (data) {
          
          if (data.msg == "sucess") {
            alertify.success("Success");
          } else {
            alertify.error("This Name Already Used");
          }
        },
        complete: function () {
          $(".preloader").css("visibility", "hidden");
        },
      });
    },
    allowOutsideClick: () => !Swal.isLoading()
  });
  
  
  
}




function deletei(image) {
  let csf = $("input[name=csrfmiddlewaretoken]").val();
  var data = {
    image: image,
  };
  
  $.ajax({
    headers: { "X-CSRFToken": csf },
    mode: "same-origin", // Do not send CSRF token to another domain.
    beforeSend: function () {
      $(".preloader").css("visibility", "visible");
    },
    url: "/deletei",
    type: "POST",
    data: data,
    dataType: "json",
    success: function (data) {
      getimages();
      
      
      if (data.msg == "sucess") {
        alertify.success("Success");
      } else {
        alertify.error("A Container Exist");
      }
    },
    complete: function () {
      $(".preloader").css("visibility", "hidden");
    },
  });
}

function stopc(container) {
  let csf = $("input[name=csrfmiddlewaretoken]").val();
  var data = {
    'container': container,
  };
  
  $.ajax({
    headers: { "X-CSRFToken": csf },
    mode: "same-origin", // Do not send CSRF token to another domain.
    beforeSend: function () {
      $(".preloader").css("visibility", "visible");
    },
    url: "/stopc",
    type: "POST",
    data: data,
    dataType: "json",
    success: function (data) {
      getcontainers();
      
      if (data.msg == "sucess") {
        alertify.success("Success");
      } else {
        alertify.error("Error");
      }
    },
    complete: function () {
      $(".preloader").css("visibility", "hidden");
      
    },
  });
}

function deletec(container) {
  let csf = $("input[name=csrfmiddlewaretoken]").val();
  var data = {
    container: container,
  };
  
  $.ajax({
    headers: { "X-CSRFToken": csf },
    mode: "same-origin", // Do not send CSRF token to another domain.
    beforeSend: function () {
      $(".preloader").css("visibility", "visible");
    },
    url: "/deletec",
    type: "POST",
    data: data,
    dataType: "json",
    success: function (data) {
      getcontainers();
      
      if (data.msg == "sucess") {
        alertify.success("Success");
      } else {
        alertify.error("Error");
      }
    },
    complete: function () {
      $(".preloader").css("visibility", "hidden");
    },
  });
}

function startc(container) {
  let csf = $("input[name=csrfmiddlewaretoken]").val();
  var data = {
    'container': container,
  };
  
  $.ajax({
    headers: { "X-CSRFToken": csf },
    mode: "same-origin", // Do not send CSRF token to another domain.
    beforeSend: function () {
      $(".preloader").css("visibility", "visible");
    },
    url: "/startc",
    type: "POST",
    data: data,
    dataType: "json",
    success: function (data) {
      getcontainers();
      if (data.msg == "sucess") {
        alertify.success("Success");
      } else {
        alertify.error("Error");
      }
    },
    complete: function () {
      $(".preloader").css("visibility", "hidden");
    },
  });
};


function getcontainers(){
  $.ajax({
    url: '/getcontainers',
    type: 'GET',
    beforeSend: function () {
      $(".preloader").css("visibility", "visible");
    },
    traditional: true,
    dataType: 'html',
    success: function(data){
      $('.containers').html("");
      $('.containers').append(data);
    },
    complete: function () {
      $(".preloader").css("visibility", "hidden");
    },
});   
};



function getimages(){
  $.ajax({
    url: '/getimages',
    type: 'GET',
    beforeSend: function () {
      $(".preloader").css("visibility", "visible");
    },
    traditional: true,
    dataType: 'html',
    success: function(data){
      $('.images').html("");
      $('.images').append(data);
    },
    complete: function () {
      $(".preloader").css("visibility", "hidden");
    },
});   
};




function pullimg() {
  let csf = $("input[name=csrfmiddlewaretoken]").val();
  Swal.fire({
    title: 'Enter the Name for The Image need to pull',
    input: 'text',
    inputAttributes: {
      autocapitalize: 'off'
    },
    showCancelButton: true,
    confirmButtonText: 'Start',
    showLoaderOnConfirm: true,
    preConfirm: (img_name) => {
      
      var data = {
        img_name: img_name,

      };
      $.ajax({
        headers: { "X-CSRFToken": csf },
        mode: "same-origin", // Do not send CSRF token to another domain.
        beforeSend: function () {
          $(".preloader").css("visibility", "visible");
        },
        url: "/pullimg",
        type: "POST",
        data: data,
        dataType: "json",
        success: function (data) {
          
          if (data.msg == "sucess") {
            alertify.success("Success");
            getimages();
          } else if (data.msg == "exist"){
            alertify.error("This image alredy exist");
          }else{
            alertify.error("error");
          }
        },
        complete: function () {
          $(".preloader").css("visibility", "hidden");
        },
      });
    },
    allowOutsideClick: () => !Swal.isLoading()
  });
  
  
  
}