// 選択した縦ラインも分かるように
$(document).ready(function(e){

	function addhover(day_class){
		$(day_class).hover(function(e){
			$(day_class).addClass('active');
		},function(e){
			$(day_class).removeClass('active');		  
		});
	}

	var d_count = $('tbody>tr:first>td').length;	//テーブルの一列目tdの総数

	for(var i=1;i<=d_count;i++){
		var d_num = i.toString();
		addhover('.day_'+d_num);
	}

});
