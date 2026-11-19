def parse_requirements(file_content):
    sbom_items = []
    lines = file_content.split('\n')
    
    for line in lines:
        line = line.strip()
        if not line or line.startswith('#'):
            continue
            
        if '==' in line:
            pkg_name, version = line.split('==', 1)
            status = "Pinned (Secure)"
        elif '>=' in line:
            pkg_name, version = line.split('>=', 1)
            version = ">=" + version
            status = "Unpinned (Warning)"
        else:
            pkg_name = line
            version = "Latest / Unspecified"
            status = "Unpinned (High Risk)"
            
        sbom_items.append({
            "Component": pkg_name.strip(),
            "Version": version.strip(),
            "Type": "Python Library",
            "SBOM Status": status
        })
        
    return sbom_items