function getinterface() {
    let csf = $("input[name=csrfmiddlewaretoken]").val();
    var html="<select class='custom-select' onchange='enablemon(this.value)'><option selected>Select the interface</option>";
    var data = {
        
      };
        $.ajax({
          headers: { "X-CSRFToken": csf },
          mode: "same-origin", // Do not send CSRF token to another domain.
          beforeSend: function () {
            $(".preloader").css("visibility", "visible");
          },
          url: "/getinterface",
          type: "POST",
          data: data,
          dataType: "json",
          success: function (data) {
            console.log(data);
            // for ( var i = 0, l = data.data.length; i < l; i++ ) {
            //     html+="<option value='"+data.data[i]+"'>"+data.data[i]+"</option>";
            // }
            
            html+="</select>"; 
            

            $(".interface").html(html);
          },
          complete: function () {
            $(".preloader").css("visibility", "hidden");
          },
        });
    
  }





  function getsettings() {
    let csf = $("input[name=csrfmiddlewaretoken]").val();
    
    var data = {
        
      };
      
        $.ajax({
          headers: { "X-CSRFToken": csf },
          mode: "same-origin", // Do not send CSRF token to another domain.
          beforeSend: function () {
            $(".preloader").css("visibility", "visible");
          },
          url: "/getsettings",
          type: "POST",
          data: data,
          success: function (data) {

           

            $(".data").html(data);
          },
          complete: function () {
            $(".preloader").css("visibility", "hidden");
          },
        });
      }
  
      function getdetector() {
        let csf = $("input[name=csrfmiddlewaretoken]").val();
        
        var data = {
            
          };
          
            $.ajax({
              headers: { "X-CSRFToken": csf },
              mode: "same-origin", // Do not send CSRF token to another domain.
              beforeSend: function () {
                $(".preloader").css("visibility", "visible");
              },
              url: "/getdetector",
              type: "POST",
              data: data,
              success: function (data) {
               
    
                $(".detector_data").html(data);
              },
              complete: function () {
                $(".preloader").css("visibility", "hidden");
              },
            });
          }


    
          function getsensorbutton() {
            let csf = $("input[name=csrfmiddlewaretoken]").val();
            
            var data = {
                
              };
              
                $.ajax({
                  headers: { "X-CSRFToken": csf },
                  mode: "same-origin", // Do not send CSRF token to another domain.
                  beforeSend: function () {
                    $(".preloader").css("visibility", "visible");
                  },
                  url: "/getsensorbutton",
                  type: "POST",
                  data: data,
                  success: function (data) {
                   
        
                    $(".sensor_button").html(data);
                  },
                  complete: function () {
                    $(".preloader").css("visibility", "hidden");
                  },
                });
              }
  
  function enablemon(interface) {
    let csf = $("input[name=csrfmiddlewaretoken]").val();
    var html="<select class='custom-select ' ><option disabled selected>Select Adapter</option>";
   
    var data = {interface:interface
        
      };
      if(interface!="" || interface !=none){
        $.ajax({
          headers: { "X-CSRFToken": csf },
          mode: "same-origin", // Do not send CSRF token to another domain.
          beforeSend: function () {
            $(".preloader").css("visibility", "visible");
          },
          url: "/enablemon",
          type: "POST",
          data: data,
          dataType: "json",
          success: function (data) {
            for ( var i = 0, l = data.mon_enb_dev.length; i < l; i++ ) {
              if(data.mon_enb_dev[i].name==interface && data.mon_enb_dev[i].status){
                alertify.success("Monitor mode Enabled");
              }else{
                alertify.error("Monitor not Enabled");
              }
              if(data.mon_enb_dev[i].status){
                html+="<option value='"+data.mon_enb_dev[i].name+"'>"+data.mon_enb_dev[i].name+"</option>";
              }
            }
            
            html+="</select>"; 

            $(".monitor_mode_devices").html(html);
         

          },
          complete: function () {
            $(".preloader").css("visibility", "hidden");
          },
        });
      }
  }

  function diseablemon(interface) {
    let csf = $("input[name=csrfmiddlewaretoken]").val();
    var html="<select class='custom-select ' ><option disabled selected>Select Adapter</option>";
    var data = {interface:interface
        
      };
      if(interface!="" || interface !=none){
        $.ajax({
          headers: { "X-CSRFToken": csf },
          mode: "same-origin", // Do not send CSRF token to another domain.
          beforeSend: function () {
            $(".preloader").css("visibility", "visible");
          },
          url: "/diseablemon",
          type: "POST",
          data: data,
          dataType: "json",
          success: function (data) {
            for ( var i = 0, l = data.mon_enb_dev.length; i < l; i++ ) {
              if(data.mon_enb_dev[i].name==interface && !data.mon_enb_dev[i].status){
                alertify.success("Monitor mode Disabled");
              }else{
                alertify.error("Monitor mode not Disabled");
              }
             
              if(data.mon_enb_dev[i].status){
                html+="<option value='"+data.mon_enb_dev[i].name+"'>"+data.mon_enb_dev[i].name+"</option>";
              }
            }
            
            html+="</select>"; 

            $(".monitor_mode_devices").html(html);
          },
          complete: function () {
            $(".preloader").css("visibility", "hidden");
          },
        });
      }
  }
  

  function saveDatabase(){
    var old_link= $('.old_link').val();
    var database_link= $('.database_link').val();
    let csf = $("input[name=csrfmiddlewaretoken]").val();
    var data = {database_link:database_link
        
    };
    
    
    if(old_link!=database_link && database_link!=""){
      $.ajax({
        headers: { "X-CSRFToken": csf },
        mode: "same-origin", 
        beforeSend: function () {
          $(".preloader").css("visibility", "visible");
        },
        url: "/saveDatabase",
        type: "POST",
        data: data,
        dataType: "json",
        success: function (data) {
         
          $('.database_link').val(data['database_link']);
          $('.old_link').val(data['database_link']);
          if (!data["err"]) {
            alertify.success(data['msg']);
          } else {
            alertify.error(data['msg']);
          }
        },
        complete: function () {
          $(".preloader").css("visibility", "hidden");
        },
      });}else{
        alertify.error("Please Make A change");
      }

  }




    

  function resetDatabase(){
    let csf = $("input[name=csrfmiddlewaretoken]").val();
    var data = {
        
    };
    
  
      $.ajax({
        headers: { "X-CSRFToken": csf },
        mode: "same-origin", // Do not send CSRF token to another domain.
        beforeSend: function () {
          $(".preloader").css("visibility", "visible");
        },
        url: "/resetDatabase",
        type: "POST",
        data: data,
        dataType: "json",
        success: function (data) {
          if(!data['error']){
            alertify.success(data['msg']);

          }else{
            alertify.error(data['msg']);
          }
        },
        complete: function () {
          $(".preloader").css("visibility", "hidden");
        },
      });

  }



  function enableDisMon(wifidev){
    let csf = $("input[name=csrfmiddlewaretoken]").val();
    if ($(".check-"+wifidev).is(":checked")) {
      enablemon(wifidev)
   }else{
      diseablemon(wifidev)
   }
    
  }


  function saveDetector(){
    let csf = $("input[name=csrfmiddlewaretoken]").val();
    var api =$('.detector_api').val();
    var api_old =$('.detector_api_old').val();
    var adapter_withmon=$('.monitor_mode_devices').val();
    var data = {
     
    };
    if(api != api_old && api !=""){

      data['api']=api
      
      
    }
    if(adapter_withmon!="" && adapter_withmon!=null){
      data['adapter_withmon']=adapter_withmon
     
    }



    
  if(Object.keys(data).length!=0){
      $.ajax({
        headers: { "X-CSRFToken": csf },
        mode: "same-origin", // Do not send CSRF token to another domain.
        beforeSend: function () {
          $(".preloader").css("visibility", "visible");
        },
        url: "/saveDetector",
        type: "POST",
        data: data,
        dataType: "json",
        success: function (data) {
          if(!data['err']){
            $('.detector_api_old').val(data['api']);
            $('.detector_api').val(data['api']);
            alertify.success(data['msg']);
          }else{
            alertify.error(data['msg']);
          }
        
          
        },
        complete: function () {
          $(".preloader").css("visibility", "hidden");
        },
      });
   
    }else{
      alertify.error("Please Make Some Changes");
    }


  }





  function start_deauth_detector(adapter){


    let csf = $("input[name=csrfmiddlewaretoken]").val();
    console.log(adapter);
    var data = {
      adapter:adapter

    };
    
  if(adapter!=""){
      $.ajax({
        headers: { "X-CSRFToken": csf },
        mode: "same-origin", // Do not send CSRF token to another domain.
        beforeSend: function () {
          $(".preloader").css("visibility", "visible");
        },
        url: "/start_deauth_detector",
        type: "POST",
        data: data,
        dataType: "json",
        success: function (data) {
         
          if(data['err']){
            alertify.error(data['message']);
          }else{
            alertify.success(data['message']);
            getsensorbutton();
          }
        },
        complete: function () {
          $(".preloader").css("visibility", "hidden");
        },
      });
   
    }else{
      console.log("please select a adapter from settings")
    }
  }


  function stop_deauth_detector(){


    let csf = $("input[name=csrfmiddlewaretoken]").val();
    
    var data = {
     

    };
    

      $.ajax({
        headers: { "X-CSRFToken": csf },
        mode: "same-origin", // Do not send CSRF token to another domain.
        beforeSend: function () {
          $(".preloader").css("visibility", "visible");
        },
        url: "/stop_deauth_detector",
        type: "POST",
        data: data,
        dataType: "json",
        success: function (data) {
         
          if(data['err']){
            alertify.error(data['message']);
          }else{
            alertify.success(data['message']);
            getsensorbutton();
          }
        },
        complete: function () {
          $(".preloader").css("visibility", "hidden");
        },
      });
   
    
  }


// function checkMonitorDev(){
//   let csf = $("input[name=csrfmiddlewaretoken]").val();
//   var html="<select class='custom-select ' ><option disabled selected>Select Adapter after enabling monitor mode</option>";
//     var data = {
        
//     };
    
  
//       $.ajax({
//         headers: { "X-CSRFToken": csf },
//         mode: "same-origin", // Do not send CSRF token to another domain.
//         beforeSend: function () {
//           $(".preloader").css("visibility", "visible");
//         },
//         url: "/checkMonitorDev",
//         type: "POST",
//         data: data,
//         dataType: "json",
//         success: function (data) {
//           console.log(data);
//           for ( var i = 0, l = data.data.length; i < l; i++ ) {
//             html+="<option value='"+data.data[i]+"'>"+data.data[i]+"</option>";
//         }
        
//         html+="</select>"; 
         
          
//         },
//         complete: function () {
//           $(".preloader").css("visibility", "hidden");
//         },
//       });


// }