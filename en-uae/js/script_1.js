//for removing duplicates from items array
function checkItem(item){
		for (i in items){
		if(items[i]==item){
			return true
		}
	}
	}

//to sanitize  the data
function sanitize(){
	//removing null indexes
	if (souq!="")
		souq.pop()
	wadi.pop()
	//sanitizing names
		// for (item in wadi){
		// 	s=wadi[item].Name
		// 	if(s.indexOf('(')!=-1)
		// 		s=s.substring(0,s.indexOf('('))
		// 	s=s.trim()
		// 	wadi[item].Name=s
			
		// }
		// for (i=0;i<souq.length;i++){
		// 	s=souq[i].Name
		// 	if(s.indexOf('(')!=-1)
		// 		s=s.substring(0,s.indexOf('('))
		// 	s=s.trim()
		// 	souq[i].Name=s
		// }
		// console.log(souq)
}
//for jumping to next device-wadi
$('#next-device').on('click',function(){
	
	$.when($.post('map.php',{item:wadi[count]['ID'],items:items,cat:category},function(data){})).then(function(){
		count+=1
		loadDevices_wadi(count)
		loadDevices_souq(count)
		$('.right-pane').empty()
		items=[]
		
	})
	

})
//for jumping back to prev device-wadi
$('#prev-device').on('click',function(){
	if(count==0)
		return;
	count-=1
	loadDevices_wadi(count)
	loadDevices_souq(count)
})

//for jumping to specific page
$('#jump-to-page').click(function(){
	page=$('#page').val()
	if(!page)
		return
	count=page-1
	loadDevices_wadi(count);
    loadDevices_souq(count);
})
mappings=""
//for checking if a device is already mapped
function checkMap(item){
	
	$.ajax({type:'POST',url:'checkmap.php',data:{item:wadi[item]['ID'],category:category},success: function(data){
		//alert(data)
		if(data=="error"){
				mappings="false"
				}
			else{
				data=JSON.parse(data)
				if(data[0]==null){
					mappings="false"
					}
				else{
					mappings=data
				}
			}
	 },async:false})
}
//for drawing already mapped items
function drawMap(map)
{
	$('.center-pane').empty()
	map.pop()


	for(i=0;i<map.length;i++){
		for (w in wadi){
			if(wadi[w]['ID']==Number(map[i]['wadi_ID']))
				break
		}
		for (s in souq){
			if(souq[s]['ID']==Number(map[i]['souq_ID']))
				break
		}
		draw(w,s,100)
	}
		
	
}

//for loading souq
function loadDevices_souq(i)
{	
	console.log(souq)
		checkMap(i)
		if(mappings!="false"){
			drawMap(mappings)
			return
		}
		$('.center-pane').empty()
		for(item in souq){
			response=[]
			response.push(compare(i,item))
			if(findAvgMatch(response,item))
				i_match.push({souqItem: item,match: match})
			
			}
			i_match.sort(function(a,b){return $(b).attr('match')-$(a).attr('match')})
			loadInacurateMatches(i_match)
			sortDevices()
			console.log("test" + mappings)
			
		
		}

//for averaging the fuzzy numbers
function findAvgMatch(response,item){
	if(response[0]=="false")
		return false
	avg=0
	c=0
	for (index in response)
	{
		if(response[index]){
			avg=avg+response[index][0][0]
			c=c+1
			console.log(response[index][0][0])}

	}
	match=Math.round((avg/c)*100,3)
	console.log(match)
	return match
	
}

//for loading fuzzy matches if no matches found based on primary condition
function loadInacurateMatches(i_match){
	if(i_match.length==1){
		//alert("No products to show")
		return
	}
	thresh=[i_match[1].match-7,i_match[1].match]
	f_match=[{}]
	for (key in i_match){
		if(i_match[key].match){
			if(i_match[key].match>=thresh[0] && i_match[key].match<=thresh[1])
				f_match.push(i_match[key])
		}
	}

	
		for (key in f_match){
			if(f_match[key].hasOwnProperty('match')){
				//$('.center-pane').append("dd")
				draw(count,f_match[key].souqItem,f_match[key].match)
			}
		}
	


}
//for drawing a matching souq device
function draw(i,item,match){
	if(souq[item].Image=="http://cf1.souqcdn.com/public/style/img/blank.gif"){
		image='img/placeholder.png'
		c='device-placeholder'
	}
	else{	
		image=souq[item].Image
		c='device-image'
	}
	price=splprice=""
	if(souq[item].Old_Price){
		splprice=souq[item].New_Price
		price=souq[item].Old_Price
	}
	else{
		price=souq[item].New_Price
		$('.device-price-new').css('display','none')
	}


	$('.center-pane').append('<div onclick="something('+souq[item].ID+')" match="' +match+ '" wadi-item="'+i+'" class="souq-device" id='+souq[item].ID+'><div class='+c+'><img src='+image+'></div><a href='+souq[item].Url+' ><div class="device-name">'+souq[item].Name+'</div></a><div class="device-price"><div class="device-price-old">Price: '+price+'</div><div class="device-price-new">Spl. Price: '+splprice+'</div></div><div class="check-overlay" id="check-'+souq[item].ID+'"></div></div>');

}

//for sorting souq devices in descreasing order of there match
function sortDevices(){

	$('.center-pane').html($('.souq-device').sort(function(a, b) {
    return $(b).attr('match') - $(a).attr('match');
}));
}
function preview(i,item){
	
	if($('#'+i+'-'+item).prop('checked')){
		$('#'+item).appendTo('.right-pane')
		items.push(item)
		}
	else if(!($('#'+i+'-'+item).prop('checked'))){
			$('#'+item).appendTo('.center-pane')
			remove(item)
	}
	
}

function remove(item){
	for (i in items){
		if(items[i]==item){
			items.splice(i,1)
			return
		}
	}
}



//for fuzzy coparing devices 
function compare(i,item)
{	response=[]
	
	souq_temp=souq[item]
	for (key in souq_temp){
		if(wadi[i].Brand!="" && souq[item].Brand!="" && wadi[i].Brand.toUpperCase()!=souq[item].Brand.toUpperCase())
			return (response.push("false"))
		if(wadi[i].OS_Version!=="" && souq[item].OS_Version!="" && wadi[i].OS_Version.toUpperCase()!=souq[item].OS_Version.toUpperCase())
			return (response.push("false"))
		if(key=="Name"){
			match=FuzzySet();
			console.log('Wadi: ' + wadi[i][key].split(/\s+/).slice(0,4).join(" "))
			console.log('Souq: ' + souq_temp[key])
			if(wadi[i][key]!="" && souq_temp[key]!=""){
				if(category=='Mobile Cases & Covers' )
					t=wadi[i][key]
				else
					t=wadi[i][key].split(/\s+/).slice(0,4).join(" ")
				if(t.indexOf('(')!=-1)
					t=t.substring(0,t.indexOf('('))
				t.trim()
				console.log("adding " + t)
				match.add(t)
				response.push(match.get(souq_temp[key].substring(0,t.length).trim()))
			}
		}

	}
	return(response)
		
}

