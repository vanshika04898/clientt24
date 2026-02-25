db = db.getSiblingDB("entry_shield");

db.students_master.createIndex(
  { studentId: 1 },
  { unique: true }
);

db.students_master.insertOne({
  studentId: "STU123",
  enrollmentNo: "2024IT001",
  fullName: "Ankit Sharma",
  gender: "MALE",

  academic: {
    course: "B.Tech",
    branch: "IT",
    semester: 5,
    session: "2024-2025"
  },

  hostel: {
    hostelName: "Hostel A",
    roomNo: "H-214",
    isHosteller: true
  },

  contact: {
    mobile: "9876543210",
    email: "ankit@university.edu"
  },

  status: "ACTIVE",
  createdAt: new Date(),
  updatedAt: new Date()
});