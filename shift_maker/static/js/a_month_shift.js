$(document).ready(function(e){

	//// 縦ラインを可視化  ////
	function setVirtical(day_num){
		var day_class = '.day_' + day_num;

		$(day_class).hover(function(){
			$(day_class).addClass('active');
		},function(){
			$(day_class).removeClass('active');		  
		});
	}

	var d_count = $('tbody>tr:first>td').length;	//テーブルの一列目tdの総数

	//// ドロップダウン ////
	function setOpen(staff_id,day_num){	//staff_idと順番は無関係だと思われるので注意,name?
		var dropdown_id = '#s' + staff_id + 'd' + day_num;
		var dropdown_menu_id = dropdown_id + '_mn';

		$(dropdown_id).hover(function(){
			$(dropdown_menu_id).dropdown('toggle');	  
		});
	}

	var s_count = $('tbody>tr>th').length;

	/* 定義した内容をセット */
	for(var i=1;i<=d_count;i++){
		var d_num = i.toString();
		setVirtical(d_num);

		for(var j=1;j<=s_count;j++){
			var s_num = j.toString();
			setOpen(s_num,d_num);		  
		}
	}

});
