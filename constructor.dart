class Team {
  String pname;
  double jno;
  String pos;
  
  Team(this.pname, this.jno, this.pos);

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

