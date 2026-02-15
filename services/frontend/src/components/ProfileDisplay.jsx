const ProfileDisplay = ({ data }) => {
  if (!data) return null;

  return (
    <div className="profile-card">
      <h3>Hello, {data.name}! Your ID is {data.user_id}.</h3>
    </div>
  );
};

export default ProfileDisplay;
