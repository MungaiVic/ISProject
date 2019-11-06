$(document).ready(function()
{
 	$('form').on('submit', function(event){
 		event.preventDefault();
 		var formData =new FormData($('form')[0]);
 		$.ajax
 		({
 			xhr: function()
 			{
				 var xhr =new window.XMLHttpRequest();	
				 //let xhr = new XMLHttpRequest();

				 xhr.upload.AddEventListener('progress',function(e){
				 	if(e.lengthComputable)
				 	{
				 		console.log('Bytes Loaded: ' + e.loaded);
				 		console.log('Total Size '+ e.total);
				 		console.log('Percentage Uploaded' =(e.loaded/e.Total));

				 		var percent = Math.round((e.loaded / e.total) * 100); 
				 		$('#progress-bar').attr('aria-valuenow', percent).css('width', percent + '%').text(percent +'%');  

				 	}

				 });

				 return xhr; 
 			},
 			type: "POST",
 			url: "/uploads",
 			processData:false,
 			contentType:false,
 			success: function ()
 			{
 				alert("File Uploaded Successfully");
 			}  
 		});
 	});
});