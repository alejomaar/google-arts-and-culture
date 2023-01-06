class Scripts:
    get_pictures_links:str = """
    var containers = [...document.querySelectorAll('.DuHQbc')];
    var img_elements = containers.map(contain => contain.firstElementChild);
    return img_elements.map(a => a.href)
    """
    
    get_pictures_images:str = """"
    var containers = [...document.querySelectorAll('.DuHQbc')];
    var img_elements= containers.map(contain => contain.firstElementChild);
    return img_elements.map(a =>window.getComputedStyle(a, false).backgroundImage)
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









