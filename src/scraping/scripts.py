class Scripts:
    scroll_down:str = "window.scrollTo(0, document.body.scrollHeight);"
    
    pictures_info:str = """
    const script = () =>{
        const containers = [...document.querySelectorAll('.DuHQbc')];
        const img_elements= containers.map(contain => contain.firstElementChild);
        return img_elements.map(img =>({
            page:img.href,
            image: window.getComputedStyle(img, false).backgroundImage
        }))  
    };
    return script()
    """
    
    get_picture_info:str = """
    var details = [...document.querySelector(".ve9nKb").querySelectorAll('li')];
    var museum = document.querySelector(".To7WBf")?.childNodes?.[0]?.textContent;
    var loc = document.querySelector(".WrfKPd")?.textContent;
    var info = details.reduce((acc,item)=>{
        const text = item.textContent;
        const chunks = text.split(':');
        const key = chunks[0];
        const value = chunks.splice(1).join("")
        return {...acc,[key]:value}
    },{})
    info['museum']= museum;
    info['location']= loc;
    return JSON.stringify(info);
    """
    

scripts = Scripts()









