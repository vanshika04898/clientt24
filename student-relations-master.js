db.student_relations_master.insertOne({
  studentId: "STU123",

  fullName: "Ramesh Kumar",
  relationType: "FATHER",

  contact: {
    mobile: "9998887776"
  },

  faceVerification: {
    photoUrl: "s3://greenform-father.jpg",
    embedding: [0.124, 0.992, 0.331],
    verifiedSource: "GREEN_FORM"
  },

  visitPermissions: {
    canVisit: true,
    canStayInGuestHouse: true
  },

  status: "ACTIVE",

  createdAt: new Date(),
  updatedAt: new Date()
});