-- ============================================
-- Simple SQL Dump File Example
-- ============================================

-- Drop table if it already exists
DROP TABLE IF EXISTS students;

-- Create a students table
CREATE TABLE students (
    id INT AUTO_INCREMENT PRIMARY KEY,
    full_name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    age INT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Insert sample student data
INSERT INTO students (full_name, email, age) VALUES
('Jean Nepo', 'nepo@example.com', 22),
('Alice Johnson', 'alice@example.com', 20),
('Michael Smith', 'michael@example.com', 24);

-- ============================================
-- End of Dump File
-- ============================================
