using System;
using System.Text;
using System.Windows.Forms;

namespace lab8
{
    public partial class Form1 : Form
    {
        Esign ds = new Esign();

        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            byte[] bytes = Encoding.ASCII.GetBytes(textBox5.Text);

            ds.Encode(bytes);
            textBox2.Text = ds.VerifSign(bytes);
            SourceText.Text = ds.GetSing();
            textBox1.Text = ds.GetHashSize().ToString();
            textBox3.Text = ds.GetSeed();
            textBox4.Text = ds.GetKeySize().ToString();
            textBox6.Text = ds.GetSignatureSize().ToString();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            textBox5.Text = "hello";
        }
    }
}
