class Team {
  String pname;
  double jno;
  String pos;
  
  Team(name, j, po){
    pname=name;
    jno=j;
    pos=po;
  }

  printdetails() {
    print('${pname} ${jno} ${pos}');
  }
}

void main() {
  var a = Team('pogba', 6.9, 'cdm');
  a.printdetails();

  var b = Team('matic', 3.1, 'cdm');
  b.printdetails();
}

