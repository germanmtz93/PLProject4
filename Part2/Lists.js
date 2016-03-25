
"use strict";

var list = function() {
    var list = function () {
        function Node(data) {
            this.data = data;
            this.next = null;
        }

        var l = {
            length: 0,
            currentNode: null,
            head: new Node(null),
            add: function(e) {
                if (l.currentNode === null) { // This is true the first time
                    l.head.data = e;
                    l.currentNode = new Node(null);
                    l.head.next = l.currentNode;
                    l.length++;
                }
                else {
                    l.currentNode.data = e;
                    var node = new Node(null);
                    l.currentNode.next = node;
                    l.currentNode = node;
                    l.length++;
                }
            },
        };

        var F = function () {
        };
        var f = new F();

        // public data
        f.run = function (e) {
            return l[e];
        };
        f.first = f.car = function () {
            return l.head.data
        };
        f.rest = f.cdr = function () {
            if(l.length > 0) {
                l.head = l.head.next;
                l.length--;
            }
            return this;
        }
        f.concat = f.cons = function(e){
            if (typeof e === 'string' || e instanceof String) {l.add(e);}
            else {
                var n = e.run('head');
                for(var i = 0; i < e.run('length'); i++) {
                    l.add(n.data);
                    n = n.next;
                }
            }
        }
        f.length = function(){return l.length};
        f.map = function(f){
            if (f instanceof Function) {
                var n = l.head;
                for(var i = 0; i < l.length; i++) {
                    n.data = f(n.data);
                    n = n.next;
                }
            }
        }

        return f;
    }();
    return list;
};

var l1 = new list();
l1.concat('a')
l1.cons('b')
document.writeln("l1: " + l1.first() + "<BR>");
document.writeln("l1: " + l1.length() + "<BR>");

var l2 = new list();
l2.cons('c')
document.writeln("<BR>l2: " + l2.car() + "<BR>");
document.writeln("l2: " + l2.length() + "<BR>");

var l3 = new list();
var l4 = new list();
l3.cons('x')
l3.cons('y')
l3.cons('z')
l4.cons(l3);
l4.cons(l3.car());

document.writeln("<BR>l3: " + l3.car());
while(l3.length() > 0) {
    document.writeln(", " + l3.cdr().car());
}

var h = l4.run('head');
document.writeln("<BR>l4: " + h.data);
for(var i = 1; i < l4.length(); i++) {
    h = h.next;
    document.writeln(", " + h.data);
}

l4.map(function(x){return x+x})
var h = l4.run('head');
document.writeln("<BR>l4: " + h.data);
for(var i = 1; i < l4.length(); i++) {
    h = h.next;
    document.writeln(", " + h.data);
}

