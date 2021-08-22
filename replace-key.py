import fileinput,sys,argparse,yaml

parser=argparse.ArgumentParser()

parser.add_argument('--file', help='Filename', required=True)
parser.add_argument('--key', help='The key to update', required=True)
parser.add_argument('--value', help='New value as is. Add quotes if required', required=True)

args=parser.parse_args()
tag=args.key
newValue = args.value


print ("{} {} ".format(tag, newValue))
with open(args.file) as f:
    doc = yaml.safe_load(f)


    key_path_list = [int(e) if e.isdigit() else e for e in tag.split(".")]
    print(key_path_list)

    depth = len(key_path_list)

    match depth:
        case 1:
           doc[key_path_list[0]]=newValue
        case 2:
           doc[key_path_list[0]][key_path_list[1]]=newValue
        case 3:
           doc[key_path_list[0]][key_path_list[1]][key_path_list[2]]=newValue
        case 4:
           doc[key_path_list[0]][key_path_list[1]][key_path_list[2]][key_path_list[3]]=newValue 
        case 5:
           doc[key_path_list[0]][key_path_list[1]][key_path_list[2]][key_path_list[3]][key_path_list[4]]=newValue 
        case 6:
           doc[key_path_list[0]][key_path_list[1]][key_path_list[2]][key_path_list[3]][key_path_list[4]][key_path_list[5]]=newValue
        case 7:
           doc[key_path_list[0]][key_path_list[1]][key_path_list[2]][key_path_list[3]][key_path_list[4]][key_path_list[5]][key_path_list[6]]=newValue
        case 8:
           doc[key_path_list[0]][key_path_list[1]][key_path_list[2]][key_path_list[3]][key_path_list[4]][key_path_list[5]][key_path_list[6]][key_path_list[7]]=newValue
        case 9:
           doc[key_path_list[0]][key_path_list[1]][key_path_list[2]][key_path_list[3]][key_path_list[4]][key_path_list[5]][key_path_list[6]][key_path_list[7]][key_path_list[8]]=newValue 
       
    print(doc)
with open(args.file, 'w') as f:
    yaml.dump(doc, f)

