var Person = { //ABSTRACT
    age: 0,
    name: '',
    setName(name) {
        if (typeof(name) === 'string' && name.length > 0) {
            this.name = name;
        }
        else return false;
    },
    setAge(age) {
        if (typeof(age) === 'number' && age > 0) {
            this.age = age;
        }
        else return false;
    },
    print() {
        console.log('name: ', this.name, ', age: ', this.age);
    }
}

Student = {
    course: 0,
    group: '',
    nextCourse() {
        this.course++;
    },
    setGroup(group) {
        if (typeof(group) === 'string' && group.length > 0) {
            this.group = group;
        }
        else return false;    
    },
    print() {
        console.log('name: ', this.name, '| age: ', this.age, '| group: ', this.group, '| course: ', this.course);
    },
}

Student.__proto__ = Person;

Teacher = {
    disciplines: [],
    addDis(dis) {
        if (typeof(dis) === 'string' && dis.length !== 0) {
            this.disciplines.push(dis);
        }
        else return false;
    },
    remDis(dis) {
        if (typeof(dis) === 'string' && dis.length !== 0 && this.disciplines.indexOf(dis) >= 0) {
            this.disciplines.splice(this.disciplines.indexOf(dis),1);
        }
        else return false;
    },
    print() {
        console.log('name: ', this.name, ', age: ', this.age, ' \n disciplines: ', this.disciplines);
    },
}

Teacher.__proto__ = Person;