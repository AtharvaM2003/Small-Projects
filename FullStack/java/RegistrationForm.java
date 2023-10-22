import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import com.mongodb.MongoClient;
import com.mongodb.client.MongoCollection;
import com.mongodb.client.MongoDatabase;
import org.bson.Document;

public class RegistrationForm extends JFrame {
    // Other form components...

    public RegistrationForm() {
        // Initialize form components...

        JButton registerButton = new JButton("Register");

        registerButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                String name = nameField.getText();
                String email = emailField.getText();
                char[] password = passwordField.getPassword();

                // Connect to MongoDB
                try (MongoClient mongoClient = new MongoClient("localhost", 27017)) {
                    MongoDatabase database = mongoClient.getDatabase("simple");
                    MongoCollection<Document> collection = database.getCollection("rege");

                    // Create a new user document
                    Document user = new Document("name", name)
                            .append("email", email)
                            .append("password", new String(password)); // Convert password to String

                    // Insert the user document into the "users" collection
                    collection.insertOne(user);

                    // Clear the form fields after registration
                    nameField.setText("");
                    emailField.setText("");
                    passwordField.setText("");
                }
            }
        });

        // Add form components...
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(new Runnable() {
            @Override
            public void run() {
                new RegistrationForm();
            }
        });
    }
}
