$(function(){

  $('#btn').click(function() {
    var r = $('input[name="level"]:checked').val();
  
    console.log(r);
  });
  
  $('input[value="普通の褒め"]').prop('checked', true);
  
  $('input[name="level"]').change(function() {
    var result = $(this).val();
    
    console.log( result );
  });
})
