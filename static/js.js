

function CheckMobile(){
    var mobile = (/iphone|ipod|android|blackberry|mini|windows\sce|palm/i.test(navigator.userAgent.toLowerCase()));  
    if (mobile) { 
        return true
    } 
    else 
    { 
       return false
    }
}



function CloseModal(){
    document.getElementById('modalcontainer').style.display = 'none';
    document.body.classList.remove("stop-scrolling");
    try{
        document.getElementById('subcontainer').style.filter = 'none';

    }catch{
        document.getElementById('container').style.filter = 'none';
    }

}

function ShowAnimation(){
    document.getElementById('animation').style.display = 'flex';
}

function ShowModal(){
    document.getElementById('modalcontainer').style.display = 'flex';
    document.getElementById('sidebardiv').style.display = 'flex';
    document.body.classList.add("stop-scrolling");
    try{
        document.getElementById('subcontainer').style.filter = 'blur(15px)';

    }catch{
        document.getElementById('container').style.filter = 'blur(15px)';
    }
    document.getElementById('usernameinput').value = '';
    document.getElementById('emailinput').value = '';
    document.getElementById('passwordinput').value = '';

}

function ShowSignup(){
    document.getElementById('emailinputdiv').style.display = 'flex';
    document.getElementById('modalloginbtn').style.borderColor = 'white';
    document.getElementById('modalsignupbtn').style.borderColor = 'aqua';

}

function ShowLogin(){
    document.getElementById('emailinputdiv').style.display = 'none';
    document.getElementById('emailinput').value = '';
    document.getElementById('modalloginbtn').style.borderColor = 'aqua';
    document.getElementById('modalsignupbtn').style.borderColor = 'white';

}

var sidebar = false

function ShowSideBar(){
    if (sidebar === false){
        document.getElementById('sidebardiv').style.display = 'flex';
        document.getElementById('sidebarbtn').style.backgroundColor = 'aqua';
        sidebar = true
    } else {
        document.getElementById('sidebardiv').style.display = 'none';
        document.getElementById('sidebarbtn').style.backgroundColor = 'black';
        sidebar = false

    }
}

var ajax_url = "http://127.0.0.1:8000/site_actions/"

function LikeMovie(id,user){
    // document.getElementById('animation').style.display = 'flex';

    // window.document.style.cursor = 'wait';
    $.ajax({
        type : 'POST',
        url : ajax_url,
        data : {
            action : 'like_movie',
            movie_id : id,
        },
        
        success : function(response){
            console.log(response['msg'])
            // window.document.style.cursor = 'none';
            if (response['msg'] === 'liked'){
                document.getElementById('likebtn'+id).innerHTML = '&#10084;';
                
            } else if (response['msg'] === 'unliked') {
                document.getElementById('likebtn'+id).innerHTML = '&#9825;';

            } else {
                console.log(response['msg'])
                ShowModal()

            }
            
        }
    })

    
    

}


function Logout(){
    document.getElementById('animation').style.display = 'flex'
    console.log('logout...')
    $.ajax({
        type: 'POST',
        url : ajax_url,
        data : {
            action : 'logout',
            
        },
        success : function(response){
            document.getElementById('animation').style.display = 'none'
            console.log('logouted')
            if (response['msg'] == 'logged out'){
                var likebtns = document.getElementsByClassName('likebtn');
                for (var i=0; i < likebtns.length; i++){
                    likebtns.item(i).innerHTML = '&#9825';
                }

                try{
                    document.getElementById('logoutdiv').style.display = 'none';
                } catch{

                }
                var check = CheckMobile()
                if (check === true){
                    document.getElementById('loginbtnajax').style.display = 'none';
                    document.getElementById('loginbtnmobile').style.display = 'flex';
                    document.getElementById('mobilelogoutbtn').style.display = 'none';
                    
                } else{
                    document.getElementById('loginbtnajax').style.display = 'flex';

                }
                document.getElementById('logoutdivajax').style.display = 'none';
                document.getElementById('favorite').style.display = 'none';

            }
            

        }
    })
}

function SubmitForm(){
    let username = document.getElementById('usernameinput').value;
    let email = document.getElementById('emailinput').value;
    let password = document.getElementById('passwordinput').value;
    document.getElementById('progressbarsignup').style.display = 'flex';
    if (username !== '' && email !== '' && password !== ''){
        $.ajax({
            type : 'POST',
            url : ajax_url,
            data : {
                action : 'signup',
                username : username,
                email : email,
                password : password
            },
            
            success : function(response){
                document.getElementById('progressbarsignup').style.display = 'none';
                CloseModal()
                
            }
        })
    } else if(username !== '' && email == '' && password !== ''){
        $.ajax({
            type : 'POST',
            url : ajax_url,
            data : {
                action : 'login',
                username : username,
                password : password
            },
            
            success : function(response){
                CloseModal()
                document.getElementById('progressbarsignup').style.display = 'none';
                if (response['msg']==='logged in'){
                    try{
                        document.getElementById('loginbtn').style.display = 'none';
                    }catch{
                        
                    }

                    for (var i=0; i < response['liked'].length; i++){
                        console.log(response['liked'][i]['id'])
                        try{

                            document.getElementById('likebtn'+response['liked'][i]['id']).innerHTML = '&#10084;';
                        }catch{
                            
                        }
                    }
                    var check = CheckMobile()
                    if (check === true){
                        
                        document.getElementById('loginbtnmobile').style.display = 'none';
                        document.getElementById('mobilelogoutbtn').style.display = 'flex';
                        document.getElementById('logoutdivajax').style.display = 'none';
                        document.getElementById('favorite').style.display = 'none';
                        document.getElementById('favoritemobile').style.display = 'flex';
                        
                    } else{
                        document.getElementById('logoutdivajax').style.display = 'flex';
                        document.getElementById('favorite').style.display = 'flex';
                        

                    }
                    document.getElementById('loginbtnajax').style.display = 'none';
                    document.getElementById('usernamelabelajax').innerHTML = response['username'];
                    document.getElementById('usernamelabelmobile').innerHTML = response['username'];

                }

            }
        })

    }
    
}


// JS for Animation
function HideProgress(){
    if (document.readyState === 'ready' || document.readyState === 'complete' ){
        console.log('Working....')
        document.getElementById('progressbar').style.display = 'none';
    }
}

function CheckLogin(){
    document.getElementById('animation').style.display = 'flex';
    $.ajax({
        type: 'POST',
        url : ajax_url,
        data : {
            action : 'check_login'
        },
        success : function(response){
            document.getElementById('animation').style.display = 'none';
            if (response['msg']=== 'true'){

                var check = CheckMobile()
                if (check === true){
                    document.getElementById('loginbtnajax').style.display = 'none';
                    document.getElementById('loginbtnmobile').style.display = 'none';
                    document.getElementById('mobilelogoutbtn').style.display = 'flex';
                    document.getElementById('favoritemobile').style.display = 'flex';
                    
                } else{
                    document.getElementById('loginbtnajax').style.display = 'flex';
                    document.getElementById('logoutdivajax').style.display = 'flex';
                    document.getElementById('favorite').style.display = 'flex';

                }

                document.getElementById('usernamelabelajax').innerHTML = response['username'];
                document.getElementById('usernamelabelmobile').innerHTML = response['username'];

            } else if (response['msg']==='false'){
                var check = CheckMobile()
                if (check === true){
                    
                    document.getElementById('loginbtnmobile').style.display = 'flex';
                    document.getElementById('favoritemobile').style.display = 'none';
                    document.getElementById('mobilelogoutbtn').style.display = 'none';
                    
                } else{
                    document.getElementById('loginbtnajax').style.display = 'flex';
                    document.getElementById('favorite').style.display = 'none';

                }
            }

        }
    })
}

function CloseTrailorModal(){
    document.getElementById('trailormodal').style.display = 'none';
    document.getElementById('contentdiv').style.filter = 'none';
    document.body.classList.remove("stop-scrolling");
    document.getElementById('player').src = '';
}

function ShowTrailorModal(src){
    document.getElementById('player').src = 'https://www.youtube.com/embed/'+src;
    document.getElementById('trailormodal').style.display = 'flex';
    document.body.classList.add("stop-scrolling");
    document.getElementById('contentdiv').style.filter = 'blur(15px)';
}

function ShowDownloadModal(){
    document.getElementById('downloadmodal').style.display = 'flex';
    document.body.classList.add("stop-scrolling");
    document.getElementById('contentdiv').style.filter = 'blur(15px)';
}

function HideDownloadModal(){
    document.getElementById('downloadmodal').style.display = 'none';
    document.getElementById('contentdiv').style.filter = 'none';
    document.body.classList.remove("stop-scrolling");
}


